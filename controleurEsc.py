import time
import os

class SysfsESCController:
    """
    Contrôleur d'ESC utilisant le sous-système natif Linux Sysfs (Hardware PWM).
    Compatible Raspberry Pi 4 et ASUS PE100A.
    """
    
    # Chemins natifs sous Linux
    PWM_CHIP = "/sys/class/pwm/pwmchip0"
    PWM_CHANNEL = f"{PWM_CHIP}/pwm0"
    
    # L'unité de base est la nanoseconde (ns)
    PERIOD_NS = 20_000_000      # 20 ms = 50 Hz (Standard ESC)
    MIN_PULSE_NS = 1_000_000    # 1 ms = Moteur arrêté (Armement)
    MAX_PULSE_NS = 2_000_000    # 2 ms = Gaz 100%

    def __init__(self):
        """Initialise et exporte la broche PWM."""
        print("Initialisation du contrôleur matériel PWM...")
        
        # 1. Vérifie si le dossier pwmchip0 existe (preuve que le dtoverlay a marché)
        if not os.path.exists(self.PWM_CHIP):
            raise RuntimeError(f"Erreur: Le contrôleur {self.PWM_CHIP} est introuvable. Avez-vous mis dtoverlay=pwm ?")
            
        # 2. Exporte le canal pwm0 pour le rendre accessible
        if not os.path.exists(self.PWM_CHANNEL):
            with open(f"{self.PWM_CHIP}/export", "w") as f:
                f.write("0")
            time.sleep(0.5) # Le temps que Linux crée le dossier virtuel
            
        # 3. Configuration de la période (50 Hz)
        self._write_file("period", str(self.PERIOD_NS))
        
        # Par sécurité, on s'assure d'envoyer un signal à 0% avant l'allumage
        self._write_file("duty_cycle", str(self.MIN_PULSE_NS))
        self._write_file("enable", "1")

    def _write_file(self, filename: str, value: str):
        """Méthode privée pour écrire dans les fichiers sysfs."""
        path = f"{self.PWM_CHANNEL}/{filename}"
        with open(path, "w") as f:
            f.write(value)

    def arm(self):
        """Séquence d'armement de sécurité de l'ESC."""
        print("\n--- ARMEMENT ---")
        print("Envoi de l'impulsion de sécurité (1 ms).")
        self._write_file("duty_cycle", str(self.MIN_PULSE_NS))
        print("Vous pouvez brancher la batterie 4S.")
        print("Attente de 6 secondes pour l'initialisation de l'ESC (bips)...")
        time.sleep(6)
        print("ESC Armé. Prêt à tourner.")

    def set_throttle(self, percentage: float):
        """Définit les gaz en pourcentage (0.0 à 100.0)."""
        if not (0.0 <= percentage <= 100.0):
            raise ValueError("Le pourcentage doit être compris entre 0 et 100.")
            
        # Interpolation mathématique
        pulse_ns = int(self.MIN_PULSE_NS + (percentage / 100.0) * (self.MAX_PULSE_NS - self.MIN_PULSE_NS))
        self._write_file("duty_cycle", str(pulse_ns))
        print(f"Gaz : {percentage}%  |  Impulsion : {pulse_ns} ns")

    def stop(self):
        """Extinction sécurisée du système."""
        print("\n--- ARRÊT ---")
        self._write_file("duty_cycle", str(self.MIN_PULSE_NS))
        time.sleep(1)
        self._write_file("enable", "0")
        print("Générateur PWM coupé. Connexion terminée.")

# === TEST DU MOTEUR ===
if __name__ == "__main__":
    try:
        # Note: Sur Raspberry Pi, Sysfs exige d'être "root" (sudo) pour modifier le matériel
        moteur = SysfsESCController()
        
        moteur.arm()
        
        # Test de poussée (15% pour éviter que le moteur ne saute de la table)
        moteur.set_throttle(15.0)
        time.sleep(3)
        
        moteur.set_throttle(25.0)
        time.sleep(3)
        
    except PermissionError:
        print("\n[ERREUR] Vous devez lancer ce script avec 'sudo' (Droits administrateur).")
    except Exception as e:
        print(f"\n[ERREUR] {e}")
    finally:
        if 'moteur' in locals():
            moteur.stop()
