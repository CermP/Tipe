# Journal de bord


## Presentation 30/01/2026

### Thème : "Sobriété, efficacité, optimisation"

### Ressources utiles :
[google scholar](https://scholar.google.fr/)

### => Apporté de la **Valeur Ajoutée** par notre travail

### Déroulé :

Problématique -> modélisation -> analytique ET experimentation ET simulation => analyse des résultats

## 06/03/2026 et 13/03/2026

Abandon des recherches sur les convertisseurs AC/DC. 

Je me suis rendu compte que le sujet était trop vaste et que je n'avais pas assez de connaissances pour pouvoir apporter une réelle valeur ajoutée. 

Sujet intéressant : hélices de drone. 
 - Trouver une meilleur compromis pour une meilleur rigidité et résistance au chocs, tout en restant assez légères pour assurer un bon fonctionnement. 
 - Optimiser le rapport poussée/consommation
 - Reperer les caractéristiques de l'hélice qui réduisent efficacité le bruit à l'utilisation.
 - Étude des impacts du materiau et de la déformation d'une hélice de drone sur son efficacité.

 -> Je selectionne le dernier point, il semble le plus intéressant et le plus réalisable dans le cadre du TIPE.

## 20/03/2026

[Présentation TIPE (PDF)](presentation/tipePresentation.pdf)

[Articles que j'ai consultés](bibliographie.md)

## 27/03/2026

[Compte rendu](presentation/compteRendu.md)

[Explication simplifiée de la "Blade Element Theory"](bladeElementTheory.md)

## 03/04/2026

[Description du banc de poussée](descriptionBancDePoussee.md)

Lecture de la section aerodynamique du site [Lavionnaire](https://lavionnaire.fr/AerodynIntro.php)

## 24/04/2026

Ecriture du protocole/experience banc de poussée

Il faudra aussi écrire le protocole de test de rigidité

## 01/05/2026

Je continue de regarder quelle architecture du banc de poussée est la plus pertinente.
J'avais penser à une cellule de charge par flexion sur laquelle est encastrée le support d'un coté et l'querre avec le moteur de l'autre, mais les vibrations du moteur pourraient perturber la mesure. aussi la structure créée un bras de levier sur la cellule de charge ce qui n'est pas désirable. ENsuite une autre structure serai avec une cellule de charge en S ou en flexion (S plus chère), le moteur est toujours surelevé avec une equerre pour evite les perturbations de l'air liées à la proximité avec le sol, et la deux solutions, soit un rail  avec le moteur et la cellule derriere, et l'hélice devant, soit, et c'est surement l'arichtecture la plus interessante pour ne pas se soucier des frottements du rail, on suspend la partie moteur/hélice à une pivot.

## 22/05/2026

Un banc de poussée avec une balance à la place du cellule de charge sera sûrment plus simple à réaliser, l'acquisition de l'effort de poussée plus mais pas coninue ? 

## 31/05/2026

**Conception du système de poussée variable à hélice sur chariot mobile coulissant**

Modélisation de la platine moteur et détermination de ses dimensions, du placement des vis et du mode d'accroche :

### 1. Dimensionnement de la platine
- **Contrainte principale :** Hélice de 5 pouces (Ø 127 mm). L'entraxe des colonnes de guidage doit être > 127 mm pour éviter toute collision et perturbation aérodynamique.
- **Entraxe des colonnes retenu :** 160 mm.
- **Dimensions finales de la platine :** 190 mm × 60 mm, épaisseur 3 ou 4 mm (aluminium).

### 2. Récapitulatif des perçages (platine moteur)
| Fonction | Position | Perçage |
|---|---|---|
| Moteur (arbre) | Centre | Ø 8 mm |
| Moteur (vis) | Centre, carré 16×16 mm | 4× M3 |
| Colonne gauche (dégagement) | −80 mm du centre (axe X) | Ø 10–12 mm |
| Colonne droite (dégagement) | +80 mm du centre (axe X) | Ø 10–12 mm |
| Bride LMK8UU gauche | −80 mm, carré 24×24 mm | 4× Ø 4,2 mm |
| Bride LMK8UU droite | +80 mm, carré 24×24 mm | 4× Ø 4,2 mm |
| Liaison plaque inférieure | 4 coins (±85 mm X / ±20 mm Y) | 4× Ø 4,2–5 mm |

### 3. Architecture du chariot (anti-arc-boutement)
Pour éviter qu'une seule plaque avec deux douilles ne s'arc-boute sous effort axial, la platine moteur forme le toit d'un caisson rigide :
- **Plaque supérieure** (platine moteur).
- **Plaque inférieure** identique (en perçages colonnes + coins), placée environ 150 mm plus bas.
- **Liaison :** Soit par tiges filetées M4 + tubes alu de 150 mm (très rigide, tubes en compression), soit par entretoises hexagonales taraudées (plus compact).

### 4. Prochaines étapes (Ancien plan abandonné)
1. Modéliser la plaque inférieure.
2. Choisir la méthode d'entretoise et modéliser les 4 éléments de liaison.
3. Vérifier que l'assemblage complet ne crée pas d'interférence avec l'hélice en rotation.

## 08/07/2026

**Changement radical d'architecture : Passage au Banc Pendulaire en "L"**

Après analyse critique du système de chariot coulissant, plusieurs problèmes majeurs ont été identifiés :
- **Aérodynamisme :** La platine de 190x60mm bloquait le flux de l'hélice, créant un effet de sillage important (turbulences et perte de poussée).
- **Frottements :** Les douilles LMK8UU sur axes généraient des frottements secs (hystérésis) estimés à ~17g d'erreur.
- **Acquisition :** L'alimentation du lycée ne suffira pas (besoin de ~40A sous 15V).

**Nouvelles décisions :**
1. Utilisation de batteries LiPo haute capacité pour assurer la puissance nécessaire.
2. Conception d'un bras de levier pendulaire en "L" (rapport 1:1) monté sur roulements à billes 608ZZ. Les frottements secs sont mathématiquement divisés par 280 (erreur théorique de 0.06g au lieu de 17g). L'obstacle aérodynamique est réduit à un simple tube carré de 20x20mm caché derrière le moteur.
3. Dans un premier temps, mesure avec une balance classique posée à plat sous le bras horizontal pour valider le concept, avant de potentiellement passer sur une cellule de charge + HX711 pour l'acquisition dynamique continue.
4. Nécessité absolue de construire une **cage de protection** en polycarbonate/grillage pour la sécurité.

**Conception SolidWorks en cours :**
- Modélisation du **Coude** (pièce d'assemblage centrale avec embouts mâles s'insérant dans les tubes alu de 20x20mm). Prise en compte des tolérances d'impression 3D (ex: trous de 8.2mm pour axes de 8mm).
- Modélisation du **Palier** (support en U fixé sur la potence, logeant les roulements à billes avec trous de 22.2mm pour emmanchement en force de roulements de 22.0mm).

---

## Campagne de conception estivale (juillet 2026)

### 22/07/2026 — Architecture mécanique

**Abandon définitif du chariot coulissant.** Les frottements secs des douilles LMK8UU sur colonnes lisses constituaient une source d'hystérésis rédhibitoire pour la mesure de poussée. L'architecture pendulaire en « L » est retenue comme solution définitive.

**Géométrie du bras pendulaire en L :**
| Paramètre | Valeur |
|---|---|
| Bras vertical (support moteur) | 140 mm |
| Bras horizontal (côté balance/cellule de charge) | 200 mm |
| Section du profilé aluminium | Tube carré 20×20 mm |
| Matériau des pièces de jonction (coude, palier) | PLA, impression 3D FDM |

**Pivot :** Pour l'instant, le pivot est réalisé par une simple vis traversant la pièce d'assemblage en PLA. Les roulements à billes 608ZZ sont disponibles mais non encore intégrés. L'objectif est de valider le concept avec cette liaison avant de migrer vers les roulements.

### 22/07/2026 — Électronique de puissance et de commande

**Composants retenus :**
| Composant | Référence | Remarques |
|---|---|---|
| Moteur brushless | T-Motor P2207 V3 (4–6S) | Stator 22×07, KV ~1950 (4S) ou ~1750 (6S) |
| Contrôleur ESC | iFlight Borg 60R | 60 A continu, BLHeli_32 |
| Microcontrôleur | Raspberry Pi 4 | Génération PWM matérielle via Sysfs |
| Alimentation | Batterie LiPo 4S | Abandon temporaire de l'alimentation stabilisée |

**État du câblage :** Les composants sont en possession. Aucune soudure n'a été réalisée. Il manque des câbles jumper (Dupont) pour connecter le GPIO du Raspberry Pi au signal PWM de l'ESC. La connexion entre l'ESC et le moteur (3 phases) nécessitera des soudures XT60/XT30 ou des connecteurs à balle.

### 22/07/2026 — Logiciel embarqué (Raspberry Pi)

Un contrôleur PWM matériel a été développé et testé en isolation (sans moteur connecté). Le script utilise l'interface Sysfs native de Linux (`/sys/class/pwm/pwmchip0`) pour générer un signal à 50 Hz. 

**Paramètres du signal PWM :**
| Paramètre | Valeur |
|---|---|
| Période | 20 ms (50 Hz) |
| Impulsion minimale (moteur arrêté) | 1,0 ms |
| Impulsion maximale (plein gaz) | 2,0 ms |

**Code source :** `controleurEsc.py` (voir ci-dessous).

```python
import time
import os

class SysfsESCController:
    """
    Contrôleur d'ESC utilisant le sous-système natif Linux Sysfs (Hardware PWM).
    Compatible Raspberry Pi 4 et ASUS PE100A.
    """
    
    PWM_CHIP = "/sys/class/pwm/pwmchip0"
    PWM_CHANNEL = f"{PWM_CHIP}/pwm0"
    
    PERIOD_NS = 20_000_000      # 20 ms = 50 Hz (Standard ESC)
    MIN_PULSE_NS = 1_000_000    # 1 ms = Moteur arrêté (Armement)
    MAX_PULSE_NS = 2_000_000    # 2 ms = Gaz 100%

    def __init__(self):
        """Initialise et exporte la broche PWM."""
        print("Initialisation du contrôleur matériel PWM...")
        
        if not os.path.exists(self.PWM_CHIP):
            raise RuntimeError(
                f"Erreur: Le contrôleur {self.PWM_CHIP} est introuvable. "
                "Avez-vous mis dtoverlay=pwm ?"
            )
            
        if not os.path.exists(self.PWM_CHANNEL):
            with open(f"{self.PWM_CHIP}/export", "w") as f:
                f.write("0")
            time.sleep(0.5)
            
        self._write_file("period", str(self.PERIOD_NS))
        self._write_file("duty_cycle", str(self.MIN_PULSE_NS))
        self._write_file("enable", "1")

    def _write_file(self, filename: str, value: str):
        path = f"{self.PWM_CHANNEL}/{filename}"
        with open(path, "w") as f:
            f.write(value)

    def arm(self):
        """Séquence d'armement de sécurité de l'ESC."""
        print("\n--- ARMEMENT ---")
        print("Envoi de l'impulsion de sécurité (1 ms).")
        self._write_file("duty_cycle", str(self.MIN_PULSE_NS))
        print("Brancher la batterie 4S.")
        print("Attente de 6 secondes pour l'initialisation de l'ESC...")
        time.sleep(6)
        print("ESC Armé. Prêt à tourner.")

    def set_throttle(self, percentage: float):
        """Définit les gaz en pourcentage (0.0 à 100.0)."""
        if not (0.0 <= percentage <= 100.0):
            raise ValueError("Le pourcentage doit être compris entre 0 et 100.")
        pulse_ns = int(
            self.MIN_PULSE_NS
            + (percentage / 100.0) * (self.MAX_PULSE_NS - self.MIN_PULSE_NS)
        )
        self._write_file("duty_cycle", str(pulse_ns))
        print(f"Gaz : {percentage}%  |  Impulsion : {pulse_ns} ns")

    def stop(self):
        """Extinction sécurisée du système."""
        print("\n--- ARRÊT ---")
        self._write_file("duty_cycle", str(self.MIN_PULSE_NS))
        time.sleep(1)
        self._write_file("enable", "0")
        print("Générateur PWM coupé. Connexion terminée.")

if __name__ == "__main__":
    try:
        moteur = SysfsESCController()
        moteur.arm()
        moteur.set_throttle(15.0)
        time.sleep(3)
        moteur.set_throttle(25.0)
        time.sleep(3)
    except PermissionError:
        print("\n[ERREUR] Lancer avec 'sudo'.")
    except Exception as e:
        print(f"\n[ERREUR] {e}")
    finally:
        if 'moteur' in locals():
            moteur.stop()
```

**Pré-requis Raspberry Pi :** Ajouter `dtoverlay=pwm,pin=18,func=2` dans `/boot/config.txt` puis redémarrer. Le script nécessite les droits `sudo`.

### 22/07/2026 — Acquisition de la poussée

**Phase 1 (POC) — Balance grand public :** Le principe de mesure par balance posée sous le bras horizontal a été validé qualitativement. La lecture reste manuelle et non continue. Cette approche est suffisante pour un premier balayage de la courbe \(T = f(\text{PWM})\) mais ne permet pas l'évaluation rigoureuse des incertitudes.

**Phase 2 (cible) — Cellule de charge HX711 :** La conception finale prévoit l'intégration d'une cellule de charge à jauges de déformation interfacée via un amplificateur HX711 avec un microcontrôleur (Arduino ou Raspberry Pi). Objectifs :
- Maîtrise de la fréquence d'échantillonnage (10–80 Hz).
- Enregistrement continu des données pour le tracé des courbes.
- Évaluation objective des incertitudes de type B (résolution, linéarité, dérive thermique du capteur).

---

## Automne 2026 — Simulation 3D SolidWorks et chaîne d'acquisition Arduino

### 04/11/2026 — Simulation par Éléments Finis (SOLIDWORKS Simulation)

Afin de valider le modèle analytique 1D codé en Python (`simulation1.py`) et de prendre en compte le couplage 3D entre la flexion et la torsion sur une géométrie vrillée, une étude statique par éléments finis a été réalisée sous **SOLIDWORKS Simulation**.

#### 1. Modélisation géométrique de la pale
La pale a été modélisée par un **bossage balayé avec torsion** reproduisant les dimensions du modèle Python (hélice $5 \times 4{,}5\text{ pouces}$) :
- **Section rectangulaire :** Corde $c = 12\text{ mm}$, épaisseur $e = 2\text{ mm}$.
- **Longueur utile de pale :** $L = 53{,}5\text{ mm}$ (du rayon de pied $r_{\min} = 10\text{ mm}$ au rayon de bout de pale $r_{\max} = 63{,}5\text{ mm}$).
- **Vrillage géométrique initial :** Torsion imposée le long de la trajectoire ($\Delta \theta_{\text{vrillage}} = 30^\circ$) pour représenter l'évolution de l'angle de calage $\theta_{\text{géo}}(r) = \arctan\left(\frac{\text{Pas}}{2\pi r}\right)$ entre le pied et le bout de pale.

#### 2. Conditions aux limites et chargement (régime de $25\,000\text{ tr/min}$)
- **Encastrement :** Géométrie fixe imposée sur la section de pied de pale ($12 \times 2\text{ mm}$).
- **Effort de poussée (flexion) :** Force normale répartie $F = 8\text{ N}$ sur l'intrados de la pale (soit $16\text{ N}$ pour l'hélice bipale complète, conformément au calcul BET à $25\,000\text{ tr/min}$).
- **Moment de torsion aérodynamique :** Couple $M_t = F \times d = 8 \times 0{,}003 = 0{,}024\text{ N}\cdot\text{m}$ autour de l'axe longitudinal de la pale (la portance s'appliquant au quart de corde, soit à $d = 0{,}25\,c = 3\text{ mm}$ de l'axe élastique).

#### 3. Résultats comparatifs : Pale rigide vs Pale souple
L'outil *Sonde* a été utilisé aux deux extrémités du bout de pale (bord d'attaque $U_1$ et bord de fuite $U_2$, espacés de $c = 12\text{ mm}$) afin de séparer la flexion moyenne $U_{\text{moy}} = \frac{U_1 + U_2}{2}$ et l'angle de détorsion en bout de pale $\Delta \phi = \arctan\left(\frac{|U_1 - U_2|}{c}\right)$ :

| Paramètre | **Pale rigide (Nylon 6/10 renforcé)** | **Pale souple (Nylon 101 pur)** |
|---|---|---|
| **Module d'Young ($E$)** | $8{,}3\text{ GPa}$ | $1{,}0\text{ GPa}$ |
| **Déplacement Bord 1 ($U_1$)** | $2{,}238\text{ mm}$ | $17{,}24\text{ mm}$ |
| **Déplacement Bord 2 ($U_2$)** | $2{,}048\text{ mm}$ | $15{,}97\text{ mm}$ |
| **Flexion moyenne en bout ($U_{\text{moy}}$)** | **$2{,}14\text{ mm}$** | **$16{,}61\text{ mm}$** |
| **Écart bord d'attaque / fuite ($\Delta U$)** | $0{,}190\text{ mm}$ | $1{,}27\text{ mm}$ |
| **Angle de détorsion en bout ($\Delta \phi$)** | **$0{,}91^\circ$** | **$6{,}04^\circ$** |

#### 4. Analyse et confrontation avec le modèle Python (`simulation1.py`)
- **Validation croisée :** Pour la pale rigide ($E = 8{,}3\text{ GPa}$, équivalent à $G \approx 3{,}0\text{ GPa}$ dans `simulation1.py`), l'angle de torsion obtenu sous SolidWorks (**$0{,}91^\circ$**) est très proche de la prédiction du modèle analytique 1D Python (**$0{,}66^\circ$**). L'écart s'explique par le couplage flexion-torsion induit par le vrillage 3D de la pale.
- **Conséquence aérodynamique :** En bout de pale ($r = 63{,}5\text{ mm}$), où l'angle géométrique initial vaut $\theta_{\text{géo}} = 16{,}0^\circ$, la pale souple en Nylon 101 perd **$6{,}04^\circ$ d'incidence** (soit plus d'un tiers de son angle d'attaque dans la zone où la vitesse linéaire $V = \omega r$ est maximale), ce qui confirme le mécanisme physique de perte de poussée.

---

### 08/11/2026 — Passage à l'architecture Arduino Uno R4 et capteurs d'acquisition

Pour fiabiliser le pilotage temps réel de l'ESC et centraliser l'acquisition des mesures (poussée + vitesse de rotation réelle) sans dépendre du système d'exploitation Linux du Raspberry Pi, la chaîne d'instrumentation est migrée vers une carte **Arduino Uno R4 Minima**.

#### Matériel commandé :
| Composant | Référence | Rôle dans le banc d'essai |
|---|---|---|
| **Microcontrôleur** | Arduino UNO R4 Minima `[ABX00080]` | Processeur ARM Cortex-M4 ($48\text{ MHz}$, logique $5\text{ V}$, port USB-C direct). Génère le signal PWM ($50\text{ Hz}$) de l'ESC et acquiert en simultané la poussée et les $\text{RPM}$. |
| **Carte de prototypage** | Arduino Proto Shield Rev3 UNO `[TSX00083]` | S'emboîte sur la Uno R4 pour souder définitivement les composants après la phase de test sur breadboard (résistance aux vibrations à $25\,000\text{ tr/min}$). |
| **Capteur de vitesse (Tachymètre)** | Capteur optique infrarouge à réflexion `TCRT5000` (comparateur LM393) | Mesure la vitesse de rotation réelle $\Omega$ ($\text{tr/min}$) par interruption matérielle en détectant un repère blanc collé sur la cloche rotative du moteur. |
| **Capteur de poussée** | Cellule de charge à jauges de déformation + Convertisseur ADC 24 bits `HX711` | Mesure continue de la force transmise par le bras horizontal du pendule en « L ». |

*(Les plaques d'essai breadboard et les câbles Dupont utilisés pour le prototypage initial sont fournis par le laboratoire du lycée).*

---

## Automne 2026 — Simulation 3D SolidWorks et chaîne d'acquisition Arduino

### 04/11/2026 — Simulation par Éléments Finis (SOLIDWORKS Simulation)

Afin de valider le modèle analytique 1D codé en Python (`simulation1.py`) et de prendre en compte le couplage 3D entre la flexion et la torsion sur une géométrie vrillée, une étude statique par éléments finis a été réalisée sous **SOLIDWORKS Simulation**.

#### 1. Modélisation géométrique de la pale
La pale a été modélisée par un **bossage balayé avec torsion** reproduisant les dimensions du modèle Python (hélice $5 \times 4{,}5\text{ pouces}$) :
- **Section rectangulaire :** Corde $c = 12\text{ mm}$, épaisseur $e = 2\text{ mm}$.
- **Longueur utile de pale :** $L = 53{,}5\text{ mm}$ (du rayon de pied $r_{\min} = 10\text{ mm}$ au rayon de bout de pale $r_{\max} = 63{,}5\text{ mm}$).
- **Vrillage géométrique initial :** Torsion imposée le long de la trajectoire ($\Delta \theta_{\text{vrillage}} = 30^\circ$) pour représenter l'évolution de l'angle de calage $\theta_{\text{géo}}(r) = \arctan\left(\frac{\text{Pas}}{2\pi r}\right)$ entre le pied et le bout de pale.

#### 2. Conditions aux limites et chargement (régime de $25\,000\text{ tr/min}$)
- **Encastrement :** Géométrie fixe imposée sur la section de pied de pale ($12 \times 2\text{ mm}$).
- **Effort de poussée (flexion) :** Force normale répartie $F = 8\text{ N}$ sur l'intrados de la pale (soit $16\text{ N}$ pour l'hélice bipale complète, conformément au calcul BET à $25\,000\text{ tr/min}$).
- **Moment de torsion aérodynamique :** Couple $M_t = F \times d = 8 \times 0{,}003 = 0{,}024\text{ N}\cdot\text{m}$ autour de l'axe longitudinal de la pale (la portance s'appliquant au quart de corde, soit à $d = 0{,}25\,c = 3\text{ mm}$ de l'axe élastique).

#### 3. Résultats comparatifs : Pale rigide vs Pale souple
L'outil *Sonde* a été utilisé aux deux extrémités du bout de pale (bord d'attaque $U_1$ et bord de fuite $U_2$, espacés de $c = 12\text{ mm}$) afin de séparer la flexion moyenne $U_{\text{moy}} = \frac{U_1 + U_2}{2}$ et l'angle de détorsion en bout de pale $\Delta \phi = \arctan\left(\frac{|U_1 - U_2|}{c}\right)$ :

| Paramètre | **Pale rigide (Nylon 6/10 renforcé)** | **Pale souple (Nylon 101 pur)** |
|---|---|---|
| **Module d'Young ($E$)** | $8{,}3\text{ GPa}$ | $1{,}0\text{ GPa}$ |
| **Déplacement Bord 1 ($U_1$)** | $2{,}238\text{ mm}$ | $17{,}24\text{ mm}$ |
| **Déplacement Bord 2 ($U_2$)** | $2{,}048\text{ mm}$ | $15{,}97\text{ mm}$ |
| **Flexion moyenne en bout ($U_{\text{moy}}$)** | **$2{,}14\text{ mm}$** | **$16{,}61\text{ mm}$** |
| **Écart bord d'attaque / fuite ($\Delta U$)** | $0{,}190\text{ mm}$ | $1{,}27\text{ mm}$ |
| **Angle de détorsion en bout ($\Delta \phi$)** | **$0{,}91^\circ$** | **$6{,}04^\circ$** |

#### 4. Analyse et confrontation avec le modèle Python (`simulation1.py`)
- **Validation croisée :** Pour la pale rigide ($E = 8{,}3\text{ GPa}$, équivalent à $G \approx 3{,}0\text{ GPa}$ dans `simulation1.py`), l'angle de torsion obtenu sous SolidWorks (**$0{,}91^\circ$**) est très proche de la prédiction du modèle analytique 1D Python (**$0{,}66^\circ$**). L'écart s'explique par le couplage flexion-torsion induit par le vrillage 3D de la pale.
- **Conséquence aérodynamique :** En bout de pale ($r = 63{,}5\text{ mm}$), où l'angle géométrique initial vaut $\theta_{\text{géo}} = 16{,}0^\circ$, la pale souple en Nylon 101 perd **$6{,}04^\circ$ d'incidence** (soit plus d'un tiers de son angle d'attaque dans la zone où la vitesse linéaire $V = \omega r$ est maximale), ce qui confirme le mécanisme physique de perte de poussée.

---

### 08/11/2026 — Passage à l'architecture Arduino Uno R4 et capteurs d'acquisition

Pour fiabiliser le pilotage temps réel de l'ESC et centraliser l'acquisition des mesures (poussée + vitesse de rotation réelle) sans dépendre du système d'exploitation Linux du Raspberry Pi, la chaîne d'instrumentation est migrée vers une carte **Arduino Uno R4 Minima**.

#### Matériel commandé :
| Composant | Référence | Rôle dans le banc d'essai |
|---|---|---|
| **Microcontrôleur** | Arduino UNO R4 Minima `[ABX00080]` | Processeur ARM Cortex-M4 ($48\text{ MHz}$, logique $5\text{ V}$, port USB-C direct). Génère le signal PWM ($50\text{ Hz}$) de l'ESC et acquiert en simultané la poussée et les $\text{RPM}$. |
| **Carte de prototypage** | Arduino Proto Shield Rev3 UNO `[TSX00083]` | S'emboîte sur la Uno R4 pour souder définitivement les composants après la phase de test sur breadboard (résistance aux vibrations à $25\,000\text{ tr/min}$). |
| **Capteur de vitesse (Tachymètre)** | Capteur optique infrarouge à réflexion `TCRT5000` (comparateur LM393) | Mesure la vitesse de rotation réelle $\Omega$ ($\text{tr/min}$) par interruption matérielle en détectant un repère blanc collé sur la cloche rotative du moteur. |
| **Capteur de poussée** | Cellule de charge à jauges de déformation + Convertisseur ADC 24 bits `HX711` | Mesure continue de la force transmise par le bras horizontal du pendule en « L ». |

*(Les plaques d'essai breadboard et les câbles Dupont utilisés pour le prototypage initial sont fournis par le laboratoire du lycée).*
