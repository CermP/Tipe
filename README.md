# TIPE — Étude de l'impact de la déformation d'une hélice de drone sur ses performances

> **Thème national 2025–2026 :** Sobriété, efficacité, optimisation.

## Objectif

Quantifier expérimentalement l'influence de la rigidité matériau sur la poussée d'hélices de drone FPV 5 pouces. L'étude compare des hélices de même géométrie (ex : Gemfan 51466) mais de matériaux différents (polycarbonate, nylon chargé carbone) afin de mettre en évidence la signature aéroélastique — la divergence de poussée induite par la déformation élastique des pales en rotation.

## Structure du projet

```
Tipe/
├── readme.md                         # Ce fichier
├── journalDeBord.md                  # Chronologie complète du projet
├── protocoleExperimental.md          # Protocole d'essai (initial + mises à jour)
├── bibliographie.md                  # Références scientifiques annotées
├── bladeElementTheory.md             # Théorie de l'élément de pale (BET)
├── explicationCodeSimulation.md      # Documentation détaillée de la simulation
├── simulation1.py                    # Simulation aéroélastique (BET + torsion)
├── controleurEsc.py                  # Contrôleur PWM pour ESC (Raspberry Pi)
├── resultat1.png                     # Résultat graphique de la simulation
├── conversation.md                   # Historique des échanges de conception
├── presentation/
│   ├── tipePresentation.pdf          # Présentation initiale (mars 2026)
│   ├── presentationFinaleV6.pdf      # Présentation finale LaTeX
│   ├── compteRendu.md                # Compte-rendu de la première présentation
│   └── ...                           # Sources LaTeX et images
└── venv/                             # Environnement Python (non versionné)
```

## Approche scientifique

Le projet repose sur trois volets complémentaires :

### 1. Modélisation analytique

Description de la Blade Element Theory (BET) et de son couplage avec un modèle de torsion élastique des pales. La documentation se trouve dans [bladeElementTheory.md](bladeElementTheory.md).

### 2. Simulation numérique

Le script [simulation1.py](simulation1.py) implémente un solveur aéroélastique itératif :
- Découpage de la pale en 50 éléments (maillage 1D).
- Calcul de la portance par BET sur chaque élément.
- Calcul du moment de torsion cumulé (intégration depuis le bout de pale).
- Déformation angulaire par la loi de torsion (module de cisaillement G, inertie de torsion J).
- Convergence itérative jusqu'à l'équilibre aéroélastique.

La documentation complète est dans [explicationCodeSimulation.md](explicationCodeSimulation.md).

**Exécution :**
```bash
cd Tipe
python3 -m venv venv
source venv/bin/activate
pip install numpy matplotlib
python simulation1.py
```

### 3. Expérimentation — Banc de poussée pendulaire

#### Architecture du banc

Le banc de poussée est un pendule en « L » :
- **Bras vertical** (140 mm) : supporte le moteur et l'hélice.
- **Bras horizontal** (200 mm) : transmet la force à l'instrument de mesure (balance ou cellule de charge).
- **Pivot** : liaison rotule au sommet, montée sur la potence fixe.

Les pièces d'assemblage (coude, palier) sont imprimées en 3D. Les tubes sont en aluminium 20×20 mm.

#### Composants électroniques

| Composant | Référence |
|---|---|
| Moteur brushless | T-Motor P2207 V3 (4–6S) |
| ESC | iFlight Borg 60R (60 A) |
| Microcontrôleur | Raspberry Pi 4 |
| Alimentation | Batterie LiPo 4S |
| Hélices | Gemfan 51466 5" bipales (PC et nylon/carbone) |

#### Contrôle du moteur

Le moteur est piloté par le script [controleurEsc.py](controleurEsc.py) qui utilise le PWM matériel du Raspberry Pi via l'interface Sysfs de Linux.

**Pré-requis Raspberry Pi :**
1. Ajouter la ligne suivante dans `/boot/config.txt` :
   ```
   dtoverlay=pwm,pin=18,func=2
   ```
2. Redémarrer le Raspberry Pi.
3. Lancer le script en mode administrateur :
   ```bash
   sudo python3 controleurEsc.py
   ```

**Séquence d'utilisation :**
1. Lancer le script (`sudo python3 controleurEsc.py`).
2. Le script envoie l'impulsion d'armement (1 ms) et attend 6 secondes.
3. Brancher la batterie LiPo pendant la phase d'attente (l'ESC émet ses bips d'initialisation).
4. Le moteur démarre aux consignes programmées (15 %, puis 25 %).
5. À la fin du script, le moteur est automatiquement coupé.

#### Acquisition de la poussée

- **Phase 1 (actuelle) :** Balance grand public sous le bras horizontal. Lecture manuelle.
- **Phase 2 (prévue) :** Cellule de charge 5 kg + amplificateur HX711 + enregistrement continu.

## Consignes de sécurité

L'utilisation d'un moteur brushless avec une hélice 5" à haute vitesse présente des risques.

- **Ne jamais** faire tourner le moteur sans cage de protection.
- **Limiter** la durée des paliers à haute puissance (> 60 %) à 5 secondes maximum (risque de surchauffe).
- **Stocker** les batteries LiPo dans un sac ignifugé. Ne jamais les laisser sans surveillance pendant la charge.
- **Connecter** systématiquement le GND commun entre le Raspberry Pi et l'ESC avant de brancher la batterie.
- **Ne jamais** approcher les mains de l'hélice en rotation, même à bas régime.

## Documentation

| Document | Description |
|---|---|
| [journalDeBord.md](journalDeBord.md) | Chronologie complète de toutes les décisions et itérations |
| [protocoleExperimental.md](protocoleExperimental.md) | Protocole d'essai détaillé avec les mises à jour estivales |
| [bladeElementTheory.md](bladeElementTheory.md) | Explication de la théorie aérodynamique utilisée |
| [explicationCodeSimulation.md](explicationCodeSimulation.md) | Documentation ligne par ligne du code de simulation |
| [bibliographie.md](bibliographie.md) | Références scientifiques annotées |

## Auteur

Projet réalisé dans le cadre du TIPE (Travaux d'Initiative Personnelle Encadrés) — Classe préparatoire.
