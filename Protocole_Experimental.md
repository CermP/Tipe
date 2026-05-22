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
*   **Capteurs :** balance ? avec amplificateur  ; Voltmètre/Ampèremètre de laboratoire pour \(U\) et \(I\) ; Machine de traction du lycée pour la caractérisation statique de la pale.

**Mode opératoire :**
1.  **Caractérisation statique :** Fixer le moyeu de chaque hélice dans la machine de traction. Appliquer un effort ponctuel à 75% du rayon de la pale et relever la flèche pour déterminer la raideur propre de l'hélice souple et de l'hélice rigide.
3.  **Acquisition dynamique :** Pour l'hélice rigide, balayer la consigne PWM de 10% à 100% par paliers de 5 secondes. À chaque palier, relever \(T\), \(U\) et \(I\). 
4.  **Comparaison :** Répéter strictement la même procédure dynamique avec chaque hélice. 

### Résultats attendus et traitement des données
Pour chaque hélice, nous calculerons la puissance électrique \(P_e = U \cdot I\) absorbée. 
Nous tracerons ensuite la courbe \(P_e = f(T)\). 
**Résultat attendu :** Les deux courbes devraient se superposer à bas régime. À haute poussée, on s'attend à ce que la dérivée de la courbe de l'hélice rigide augmente fortement (chute du rendement), tandis que celle de l'hélice flexible devrait rester plus linéaire. L'écart entre les deux courbes mettra en évidence le gain énergétique dû au pas adaptatif passif.

### Liste du matériel nécessaire
*   **Électronique de puissance :** Moteur Brushless KV2400 environ, ESC 40A.
*   **Électronique de commande/mesure :** Carte Arduino Uno, module HX711, cellule de charge 5 kg.
*   **Consommables :** 2 paires d'hélices bipales 5 pouces de même modèle (ex: Gemfan 51466) mais de matériaux différents (ex: Polycarbonate vs Nylon/Carbone).
*   **Matériel du lycée :** Alimentation stabilisée haute puissance (pour éviter d'utiliser des batteries LiPo dangereuses), multimètres, machine de traction.

### Matériels à fabriquer et moyens de fabrication (voir schéma)
*   **Structure du banc :** À fabriquer au labo de SI. La potence en profilés d'aluminium (type Bosch 40x40 ou 40x80) pour garantir une rigidité absolue. Le balancier sera un tube d'aluminium léger. 
*   **Pivot glissant de guidaga de l'axe :** axe ?
***
 