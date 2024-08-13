# Déploiement d'un projet Flask avec Cloudflare Tunnel

## Prérequis

- Avoir un accès SSH à votre serveur Linux.
- Avoir un domaine enregistré.
- Avoir un compte Cloudflare configuré pour votre domaine.

## Étapes

### 1. Cloner le dépôt Git

Commencez par cloner votre dépôt Git dans le répertoire souhaité sur votre serveur.

```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

### 2. Créer et activer un environnement virtuel Python
Créez un environnement virtuel pour isoler les dépendances de votre projet.

bash
python3 -m venv venv
source venv/bin/activate

### 3. Installer les dépendances
Installez toutes les dépendances nécessaires à partir du fichier requirements.txt.

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données
Initialisez la base de données et appliquez les migrations si vous utilisez SQLAlchemy.

```bash
flask db init
flask db migrate
flask db upgrade
```

### 4. Lancer l'application
Lancez l'application avec cette commande.

```bash
gunicorn --chdir src/ --workers 3 --bind 0.0.0.0:8000 "app:create_app()"
```

### 6. Configurer le fichier config.yml pour Cloudflare Tunnel
Créez un fichier de configuration pour Cloudflare Tunnel.

```bash
sudo nano /etc/cloudflared/config.yml
```

Ajoutez les configurations suivantes :

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /home/maxtag/.cloudflared/<TUNNEL_ID>.json

ingress:
  - hostname: melmi.fr
    service: http://localhost:8000
  - service: http_status:404
Remplacez <TUNNEL_ID> par l'ID de votre tunnel.
```

### 7. Lancer l'application Flask
Assurez-vous que votre application Flask écoute sur le port 8000. Modifiez le fichier app.py ou run.py si nécessaire :

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

Lancez ensuite votre application :

```bash
flask run --host=0.0.0.0 --port=8000
```

### 8. Installer et configurer Cloudflare Tunnel
Installez Cloudflare Tunnel sur votre serveur :

```bash
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
```

### 9. Lancer Cloudflare Tunnel en tant que service
Pour s'assurer que le tunnel Cloudflare démarre automatiquement au démarrage du système, installez-le en tant que service :

```bash
sudo cloudflared service install
sudo systemctl start cloudflared
```

### 10. Configurer le DNS sur Cloudflare
Connectez-vous à votre tableau de bord Cloudflare.
Accédez à la section DNS de votre domaine melmi.fr.
Ajoutez un enregistrement CNAME avec les détails suivants :

```
Name : @
Target : <TUNNEL_ID>.cfargotunnel.com
Proxy Status : Activé (icône de nuage orange).
```

### 11. Tester le déploiement
Accédez à votre domaine https://melmi.fr pour vérifier que l'application est correctement exposée et fonctionne.
