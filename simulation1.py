import numpy as np
import matplotlib.pyplot as plt

# Constantes (Hélice APC 5x4.5E)
RHO = 1.225
R_MAX = 0.0635
R_MIN = 0.010
PITCH = 4.5 * 0.0254
N_ELEMENTS = 50

CORDE_CONSTANTE = 0.012
EPAISSEUR_PALE = 0.002
I_TORSION = (CORDE_CONSTANTE * EPAISSEUR_PALE**3) / 3.0
D_LEVIER = CORDE_CONSTANTE * 0.25 
PENTE_PORTANCE = 2 * np.pi

# Modules de cisaillement G (estimés)
G_NYLON = 1.0e9
G_CARBONE = 3.0e9

# Plage d'étude : 5k à 25k RPM
OMEGAS_RPM = np.linspace(5000, 25000, 30)
OMEGAS_RAD = OMEGAS_RPM * (2 * np.pi / 60)

def discretiser_pale(r_min, r_max, n_elements, pitch):
    rayons = np.linspace(r_min, r_max, n_elements)
    dr = (r_max - r_min) / (n_elements - 1)
    # Vrillage géométrique (pas constant)
    theta_geo = np.arctan(pitch / (2 * np.pi * rayons))
    return rayons, dr, theta_geo

def calcul_aeroelastique(rayons, dr, theta_geo, omega, module_G, max_iter=50, tolerance=1e-5):
    theta_eff = theta_geo.copy()
    V = omega * rayons
    
    for iteration in range(max_iter):
        theta_eff_old = theta_eff.copy()
        
        # Aérodynamique (BET)
        cz = PENTE_PORTANCE * theta_eff
        dT = 0.5 * RHO * CORDE_CONSTANTE * cz * (V**2) * dr
        
        # Moment de torsion
        Mt = np.zeros_like(rayons)
        for i in range(len(rayons)):
            Mt[i] = np.sum(dT[i:]) * D_LEVIER
            
        # Déformation RDM
        dphi = (Mt / (module_G * I_TORSION)) * dr
        phi = np.cumsum(dphi)
        
        # Mise à jour
        theta_eff = theta_geo - phi
        theta_eff = np.maximum(theta_eff, 0.0)
        
        erreur = np.max(np.abs(theta_eff - theta_eff_old))
        if erreur < tolerance:
            break
            
    poussee_totale = np.sum(dT) * 2
    return poussee_totale, theta_eff

if __name__ == "__main__":
    rayons, dr, theta_geo = discretiser_pale(R_MIN, R_MAX, N_ELEMENTS, PITCH)
    
    T_nylon = []
    T_carbone = []
    
    for omega in OMEGAS_RAD:
        T_n, _ = calcul_aeroelastique(rayons, dr, theta_geo, omega, G_NYLON)
        T_c, _ = calcul_aeroelastique(rayons, dr, theta_geo, omega, G_CARBONE)
        T_nylon.append(T_n)
        T_carbone.append(T_c)
        
    T_nylon = np.array(T_nylon)
    T_carbone = np.array(T_carbone)
    delta_T = T_carbone - T_nylon
    
    # Affichage
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(OMEGAS_RPM, T_carbone, 'k-', linewidth=2, label='Carbone')
    plt.plot(OMEGAS_RPM, T_nylon, 'b--', linewidth=2, label='Nylon')
    plt.title("Poussée")
    plt.xlabel("RPM")
    plt.ylabel("T (N)")
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(OMEGAS_RPM, delta_T, 'r-', linewidth=2)
    plt.fill_between(OMEGAS_RPM, 0, delta_T, color='red', alpha=0.2)
    plt.title(r"Écart $\Delta T$")
    plt.xlabel("RPM")
    plt.ylabel(r"$\Delta T$ (N)")
    plt.grid(True)
             
    plt.tight_layout()
    plt.savefig('resultatStrategie1.png')
    
    print(f"Poussée Carbone (25k RPM): {T_carbone[-1]:.2f} N")
    print(f"Poussée Nylon   (25k RPM): {T_nylon[-1]:.2f} N")
    print(f"Delta T                  : {delta_T[-1]:.2f} N")
