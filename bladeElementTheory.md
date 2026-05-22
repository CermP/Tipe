# Modélisation Aérodynamique : Théorie de l'Élément de Pale (B.E.T)

La Théorie de l'Élément de Pale (Blade Element Theory) permet de modéliser les efforts aérodynamiques générés par une hélice en rotation. Le principe consiste à assimiler la pale à une voilure d'envergure finie, découpée en sections infinitésimales indépendantes.  

## Modèle Aérodynamique Local

L'effort fondamental en aérodynamique est la portance (ou force de sustentation). Pour une voilure évoluant dans un fluide, la portance $F_z$ est donnée par la relation :

$$F_z = \frac{1}{2} \cdot \rho \cdot S \cdot V^2 \cdot C_z$$

*   $\rho$ : Masse volumique du fluide (air $\approx 1.225 \text{ kg/m}^3$)
*   $S$ : Surface de référence du profil aérodynamique ($\text{m}^2$)
*   $V$ : Vitesse relative de l'écoulement par rapport au profil ($\text{m/s}$)
*   $C_z$ : Coefficient de portance (adimensionnel). Ce paramètre dépend du profil et de son **angle d'incidence** $\theta$ (angle entre la corde du profil et le vecteur vitesse relative). Un modèle linéaire classique pose $C_z \approx a \cdot \theta$.

## Cinématique de la Pale en Rotation

Contrairement à une voilure fixe (aile d'avion), la vitesse d'une pale d'hélice n'est pas uniforme. Dans le référentiel terrestre (cas du banc d'essai statique), la vitesse relative d'une section dépend de sa distance $r$ au centre de rotation.

Pour un élément de pale infinitésimal de largeur $dr$ situé au rayon $r$ :
*   La vitesse circonférentielle est $V = \omega \cdot r$ (où $\omega$ est la vitesse angulaire de l'hélice en rad/s).
*   La surface de l'élément est $dS = c(r) \cdot dr$ (où $c(r)$ est la corde du profil, représentant la largeur de la pale au rayon $r$).

## Poussée Élémentaire

En appliquant la formule de la portance à l'élément infinitésimal $dr$, on exprime la poussée élémentaire $dT$ (composante verticale de la portance alignée avec l'axe de rotation) :

$$dT = \frac{1}{2} \cdot \rho \cdot (c(r) \cdot dr) \cdot (\omega \cdot r)^2 \cdot C_z(r)$$

Soit sous forme différentielle :
$$dT = \frac{1}{2} \rho \, c(r) \, C_z(r) \, \omega^2 \, r^2 \, dr$$

## Obtention de la Poussée Globale

La poussée totale $T$ d'une pale est obtenue par intégration de l'effort élémentaire $dT$ sur l'ensemble de son envergure, du rayon primitif de moyeu $R_{min}$ jusqu'au rayon extérieur $R_{max}$.

$$T = \int_{R_{min}}^{R_{max}} \frac{1}{2} \rho \, c(r) \, C_z(r) \, \omega^2 \, r^2 \, dr$$

*Hypothèse simplificatrice :* En admettant que la pale possède une corde constante $c$ et un angle d'incidence (donc $C_z$) constant, l'expression de la poussée totale par pale devient :
$$T = \frac{1}{2} \rho \, c \, C_z \, \omega^2 \int_{0}^{R_{max}} r^2 \cdot dr = \frac{1}{2} \rho \, c \, C_z \, \omega^2 \left[ \frac{R_{max}^3}{3} \right]$$
La poussée est proportionnelle au carré de la vitesse de rotation $\omega^2$ et au cube du rayon de l'hélice.

---

## Couplage Aéroélastique (Application au TIPE)

Le modèle analytique standard présuppose une hélice infiniment rigide géométriquement, induisant un angle d'incidence $\theta(r)$ invariable sous contrainte.  

L'utilisation d'une hélice présentant un faible module d'Young $E$ (typiquement des matériaux imprimés en 3D par FDM) implique une **flexion de la pale par chargement aérodynamique**.

Compte tenu de l'évolution du terme $V^2$ selon la distribution radiale $r^2$, la répartition des charges $dT$ est maximale en bout de pale. Ce chargement induit :
1. Une flexion de la pale de type poutre en console.
2. Une torsion matérielle associée, modifiant la géométrie locale.
3. Une baisse significative de l'angle d'incidence effectif $\theta(r)$ en bout de pale.

Cette diminution de l'incidence abaisse la valeur locale de $C_z(r)$. Or, selon l'expression différentielle, la majeure partie de l'effort $T$ est générée aux rayons élevés.  
Ainsi, **la déformation structurelle sous charge provoque une chute du coefficient de portance là où l'efficacité devrait être maximale**, conduisant à un effondrement du rendement propulsif global de l'hélice par rapport au modèle théorique nominal.
