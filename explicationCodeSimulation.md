# Explication Détaillée de la Simulation Aéroélastique (Simulation 1)

Ce document explique le fonctionnement du script `simulation1.py` bloc par bloc. C'est ce code qui constitue le cœur de la modélisation numérique du TIPE.

## 1. Importation des bibliothèques
```python
import numpy as np
import matplotlib.pyplot as plt
```
* `numpy` (np) : Permet de faire des calculs mathématiques rapides sur des listes de nombres (tableaux). Idéal pour calculer la force sur tous les segments de l'hélice d'un seul coup.
* `matplotlib.pyplot` (plt) : Utilisé pour générer les graphiques de résultats.

## 2. Constantes Physiques et Géométriques
```python
RHO = 1.225
R_MAX = 0.0635       # Rayon (5 pouces)
R_MIN = 0.010        # Rayon du moyeu
PITCH = 4.5 * 0.0254 # Pas de 4.5 pouces converti en mètres
N_ELEMENTS = 50
```
* `RHO` : Masse volumique de l'air standard (en $kg/m^3$).
* `R_MAX` / `R_MIN` : Les limites physiques de l'hélice. $0.0635\text{ m} = 6.35\text{ cm} = 2.5\text{ pouces}$ de rayon (donc 5 pouces de diamètre).
* `PITCH` : Le "pas" de l'hélice (l'avance théorique pour 1 tour), converti de pouces en mètres.
* `N_ELEMENTS` : Le nombre de "tranches" dans lesquelles on découpe la pale pour l'intégration.

```python
CORDE_CONSTANTE = 0.012
EPAISSEUR_PALE = 0.002
I_TORSION = (CORDE_CONSTANTE * EPAISSEUR_PALE**3) / 3.0
D_LEVIER = CORDE_CONSTANTE * 0.25 
PENTE_PORTANCE = 2 * np.pi
```
* `CORDE_CONSTANTE` / `EPAISSEUR_PALE` : La largeur ($1.2\text{ cm}$) et l'épaisseur moyenne ($2\text{ mm}$) de la pale.
* `I_TORSION` : Constante de torsion pour une section rectangulaire fine. C'est la résistance géométrique à la torsion.
* `D_LEVIER` : La distance entre le point où l'air pousse (à 25% de la pale) et le "squelette" central de la pale. C'est ce levier qui cause la torsion.
* `PENTE_PORTANCE` : Le coefficient directeur $a$ de la portance aérodynamique.

```python
G_NYLON = 1.0e9    
G_CARBONE = 3.0e9  
```
* Les "Modules de Cisaillement" ($G$) définissent la résistance matérielle à la torsion (1 GPa pour Nylon, 3 GPa pour Carbone). C'est ici que tu mettras les valeurs que tu mesureras expérimentalement.

## 3. Découpage de la pale (Maillage)
```python
def discretiser_pale(r_min, r_max, n_elements, pitch):
    rayons = np.linspace(r_min, r_max, n_elements)
    dr = (r_max - r_min) / (n_elements - 1)
    theta_geo = np.arctan(pitch / (2 * np.pi * rayons))
    return rayons, dr, theta_geo
```
* Cette fonction découpe le rayon en 50 morceaux (`dr`).
* `theta_geo` : Calcule l'angle de fabrication de l'hélice pour chaque tronçon. L'angle est fort près du centre (petit rayon) et faible au bout, ce qui est typique des hélices réelles.

## 4. Le Solveur Aéroélastique (Le Cœur du Programme)
```python
def calcul_aeroelastique(rayons, dr, theta_geo, omega, module_G, max_iter=50, tolerance=1e-5):
    theta_eff = theta_geo.copy()
    V = omega * rayons
```
* On initialise l'angle effectif (`theta_eff`) à l'angle de fabrication (`theta_geo`). On suppose au départ que l'hélice ne plie pas.
* `V` : Vitesse locale du vent pour chaque tronçon (vitesse = rotation $\times$ rayon).

```python
    for iteration in range(max_iter):
        theta_eff_old = theta_eff.copy()
```
* Début de la boucle itérative. On sauvegarde l'ancien angle pour vérifier si on a atteint l'équilibre.

```python
        cz = PENTE_PORTANCE * theta_eff
        dT = 0.5 * RHO * CORDE_CONSTANTE * cz * (V**2) * dr
```
* **Théorie de l'élément de pale (B.E.T)** : On calcule la portance (`dT`) sur chaque tronçon en fonction de la vitesse $V^2$ et de l'angle actuel `theta_eff`.

```python
        Mt = np.zeros_like(rayons)
        for i in range(len(rayons)):
            Mt[i] = np.sum(dT[i:]) * D_LEVIER
```
* **Calcul du moment de torsion (`Mt`)** : À un point donné de la pale, l'effort qui la tord provient de toute la force aérodynamique située *plus loin* vers le bout de la pale. On fait donc la somme des `dT` restants multipliés par le bras de levier.

```python
        dphi = (Mt / (module_G * I_TORSION)) * dr
        phi = np.cumsum(dphi)
```
* **Déformation** : `dphi` est l'angle de torsion pour un minuscule tronçon. La déformation totale `phi` s'accumule de la base vers le sommet (fonction `np.cumsum` = somme cumulée).

```python
        theta_eff = theta_geo - phi
        theta_eff = np.maximum(theta_eff, 0.0)
```
* L'hélice s'aplatit sous la charge : le nouvel angle est l'angle de fabrication *moins* l'angle de torsion.
* `np.maximum(..., 0.0)` : Assure que l'angle ne devient pas négatif (ce qui ferait planter le vol physiquement).

```python
        erreur = np.max(np.abs(theta_eff - theta_eff_old))
        if erreur < tolerance:
            break
```
* Condition d'arrêt : si l'angle n'a quasiment plus bougé par rapport au calcul précédent (inférieur à la tolérance), on a trouvé le point d'équilibre physique, on arrête la boucle.

## 5. Exécution et Balayage des Vitesses
```python
    for omega in OMEGAS_RAD:
        T_n, _ = calcul_aeroelastique(rayons, dr, theta_geo, omega, G_NYLON)
        T_c, _ = calcul_aeroelastique(rayons, dr, theta_geo, omega, G_CARBONE)
```
* Le bloc principal (`if __name__ == "__main__":`) lance la simulation pour des vitesses allant de 5 000 à 25 000 tr/min.
* Pour chaque vitesse `omega`, on appelle le solveur pour l'hélice souple (Nylon) et l'hélice rigide (Carbone).

```python
    delta_T = T_carbone - T_nylon
```
* On calcule la fameuse **Signature Aéroélastique** (la différence de poussée $\Delta T$ induite par la différence de rigidité des matériaux). Le reste du code ne sert qu'à paramétrer l'affichage `matplotlib`.
