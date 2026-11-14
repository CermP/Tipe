# Protocoles expérimental
## Impact de la déformation d'une hélice de drone sur ses performances

### Problématique
À partir de quelle vitesse de fonctionnement la déformation élastique d'une hélice de drone modifie-t-elle la poussée produite ?

### Contexte de l'expérience
Les modèles aérodynamique utilisés pour décirre les performances des hélices comme la théorie de l'élément de pôle suppose que celle-ci est indéformable. En réalité, les hélices de drone grand public sont flexibles. Cette flexibilité tend à diminuer l'angle d'incidence de l'hélice en bout de pale et modifie don le rendement de l'hélice à haut régime? Le but de mon TIPE est de quantifier ce phénomène pour des hélice de drone FPV de 5 pouces, pour connaitre quantitativement à partitr de quelles conditions tel matériau d'hélice est plus interessant qu'un autre.

### Objectif de l'expérience
Mettre en place un banc de poussée pour mesurer expérimentalement l'influence de la rigidité sur la poussée, avec différentes hélices bipales de 5 pouces, de même géométrie mais de matériaux différents (polycarbonate, nylon/carbone, etc)

### Protocole expérimental détaillé

**Grandeurs étudiées :**
*   **Grandeur de consigne (imposée) :** Le rapport cyclique (PWM) commandant la vitesse de rotation.
*   **Grandeurs mesurées :** 
    *   La poussée axiale \(T\) (en Newton).
    *   La tension \(U\) et l'intensité \(I\) consommées par le moteur.
    *   (La raideur statique de la pale (en N/m) hors fonctionnement) -> non .

**Moyens de mesure et d'action (Capteurs/Actionneurs) :**
*   **Actionneurs :** Microcontrôleur (Arduino) générant le PWM, Onduleur (ESC 40A), Moteur Brushless (stator type 2207).
*   **Capteurs :** Balance de précision (pour la V1) ou Cellule de charge avec amplificateur HX711 (pour la V2 dynamique) ; Voltmètre/Ampèremètre de laboratoire (ou capteurs ACS758) pour \(U\) et \(I\) ; Machine de traction du lycée pour la caractérisation statique de la pale.

**Mode opératoire :**
1.  **Caractérisation statique :** Fixer le moyeu de chaque hélice dans la machine de traction. Appliquer un effort ponctuel à 75% du rayon de la pale et relever la flèche pour déterminer la raideur propre de l'hélice souple et de l'hélice rigide.
3.  **Acquisition dynamique :** Pour l'hélice rigide, balayer la consigne PWM de 10% à 100% par paliers de 5 secondes. À chaque palier, relever \(T\), \(U\) et \(I\). 
4.  **Comparaison :** Répéter strictement la même procédure dynamique avec chaque hélice. 

### Résultats attendus et traitement des données
Pour chaque hélice, nous calculerons la puissance électrique \(P_e = U \cdot I\) absorbée. 
Nous tracerons ensuite la courbe \(P_e = f(T)\). 
**Résultat attendu :** Les deux courbes devraient se superposer à bas régime. À haute poussée, on s'attend à ce que la dérivée de la courbe de l'hélice rigide augmente fortement (chute du rendement), tandis que celle de l'hélice flexible devrait rester plus linéaire. L'écart entre les deux courbes mettra en évidence le gain énergétique dû au pas adaptatif passif.

### Liste du matériel nécessaire
*   **Électronique de puissance :** Moteur Brushless KV2400 environ, ESC 40A, Batteries LiPo 4S haute capacité (nécessaire car les alims de lycée ne peuvent pas fournir 40A/600W).
*   **Électronique de commande/mesure :** Carte Arduino Uno, (Module HX711 + cellule de charge 5 kg pour la version finale), Balance classique pour la V1.
*   **Consommables :** 2 paires d'hélices bipales 5 pouces de même modèle (ex: Gemfan 51466) mais de matériaux différents (ex: Polycarbonate vs Nylon/Carbone).
*   **Matériel du lycée/Sécurité :** Multimètres, machine de traction. Sac ignifugé pour LiPo, chargeur LiPo.

### Matériels à fabriquer et moyens de fabrication (voir schémas CAO)
*   **Structure du banc :** À fabriquer au labo de SI. La potence en profilés d'aluminium (type Bosch 20x20 ou 40x40) pour garantir une rigidité absolue. Le bras mobile sera un profilé d'aluminium léger de 20x20mm limitant la trainée aérodynamique.
*   **Mécanisme Pivot Pendulaire :** Assemblage coudé en L sur roulements à billes 608ZZ (pour annuler les frottements secs). Pièces de jonction (Coude, Palier) à modéliser sur SolidWorks et imprimer en 3D (PETG).
*   **Sécurité (CRITIQUE) :** Fabrication d'une cage de protection en grillage fin ou polycarbonate autour de la zone de test.
***

---

## Mise à jour — Campagne de conception estivale (juillet 2026)

Les modifications suivantes ont été apportées au protocole initial à la suite de la phase de conception estivale. Les sections précédentes sont conservées en l'état à titre d'historique.

### Modifications de l'architecture mécanique

Le système de chariot coulissant sur colonnes lisses avec douilles LMK8UU a été abandonné. La source principale du rejet est le frottement sec de la liaison glissière, introduisant une hystérésis de mesure estimée à ~17 g, incompatible avec la résolution requise pour différencier l'effet de la rigidité de la pale.

**Architecture retenue — Banc pendulaire en « L » :**
- Bras vertical (support moteur) : 140 mm.
- Bras horizontal (bras de mesure) : 200 mm.
- Section des tubes : aluminium 20×20 mm.
- Pièces d'assemblage (coude, palier) : PLA, impression 3D FDM.
- Pivot actuel : vis dans la pièce PLA (liaison pivot simple). Migration prévue vers roulements à billes 608ZZ.

Le rapport de bras n'est plus nécessairement 1:1 (140:200). Le couple de poussée au pivot sera converti en force sur la balance via le rapport géométrique.

### Modifications de l'électronique

| Élément | Protocole initial | Protocole révisé |
|---|---|---|
| Moteur | Brushless KV2400 (non spécifié) | T-Motor P2207 V3, 4–6S |
| ESC | ESC 40A (non spécifié) | iFlight Borg 60R (60 A continu) |
| Commande | Arduino Uno (PWM logiciel) | Raspberry Pi 4 (PWM matériel Sysfs) |
| Alimentation | Alimentation stabilisée de lycée | Batterie LiPo 4S |

Le passage à un Raspberry Pi permet l'utilisation du Hardware PWM natif du SoC (interface Sysfs), éliminant le jitter logiciel. Un contrôleur Python (`controleurEsc.py`) a été développé et testé en isolation. Le script génère un signal PWM à 50 Hz avec une plage d'impulsion de 1,0 ms (arrêt) à 2,0 ms (plein gaz). Pré-requis : `dtoverlay=pwm,pin=18,func=2` dans `/boot/config.txt`, exécution en `sudo`.

**État du câblage :** Composants reçus, aucune soudure réalisée. Câbles jumper manquants pour la liaison GPIO→ESC.

### Modifications de l'acquisition

**Phase 1 — Validation par balance (en cours) :**
La mesure de poussée est réalisée par une balance grand public positionnée sous l'extrémité du bras horizontal. La lecture est manuelle et ponctuelle. Cette phase sert exclusivement à valider le fonctionnement mécanique du banc et à obtenir un ordre de grandeur de la poussée.

**Phase 2 — Cellule de charge HX711 (prévue) :**
La balance sera remplacée par une cellule de charge à jauges de déformation (5 kg) interfacée avec un amplificateur HX711 et un microcontrôleur (Arduino ou Raspberry Pi). Cette configuration permettra :
- Un enregistrement continu synchronisé de la poussée et de la consigne PWM.
- Une fréquence d'échantillonnage contrôlée (10 à 80 Hz selon le gain du HX711).
- Une évaluation des incertitudes de type B conformément au GUM (résolution ADC, linéarité, hystérésis du capteur, dérive thermique).

### Mode opératoire révisé

1. **Caractérisation statique des pales :** Inchangée (machine de traction du lycée).
2. **Montage du moteur et de l'hélice :** Fixation sur la platine en bout de bras vertical du pendule.
3. **Armement :** Exécution de la séquence `arm()` du contrôleur (impulsion 1 ms pendant 6 s, temps d'initialisation de l'ESC).
4. **Balayage en consigne :** Paliers de PWM de 10 % à 80 % par incréments de 5 %, durée de chaque palier limitée à 5 secondes (contrainte thermique du moteur en régime statique).
5. **Relevé :** Lecture de la balance (phase 1) ou enregistrement continu (phase 2) à chaque palier.
6. **Répétition :** Procédure identique pour chaque hélice testée (même géométrie, matériau différent).
7. **Arrêt :** Exécution de la séquence `stop()` du contrôleur (retour à 1 ms, désactivation du PWM).