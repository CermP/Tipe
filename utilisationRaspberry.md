# Guide d'Utilisation du Raspberry Pi

## 1. Connexion & Identification Réseau

### Trouver l'adresse IP
Pour identifier l'adresse IP du Raspberry Pi sur le réseau local, cherchez une adresse MAC commençant par `e4:5f:01` :
```bash
arp -a
```

Pour vérifier la présence ou scanner l'hôte :
```bash
sudo nmap -sn <adresse_ip_du_raspberry>
```

### Identifiants par défaut
* **Mot de passe :** `raspberry`

### Déconnexion SSH
Pour fermer la session SSH :
```bash
exit
```

---

## 2. Configuration Wi-Fi (Ajout d'un réseau)

Pour ajouter un nouveau réseau Wi-Fi au Raspberry Pi avant de vous déplacer (afin qu'il s'y connecte automatiquement au démarrage) :

```bash
sudo nmcli connection add type wifi con-name "NOM_DU_RESEAU" ifname wlan0 ssid "NOM_DU_RESEAU" wifi-sec.key-mgmt wpa-psk wifi-sec.psk "MOT_DE_PASSE"
```