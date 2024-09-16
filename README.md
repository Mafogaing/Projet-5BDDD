# Projet-5BDDD

Projet du cours 5BDDD (création des API et BDD)
Utilisation de _FastAPI_

## installation Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

Désactivation de l'environnement virtuel
```bash
deactivate
````

Démarrage de l'application main.py
```bash
fastapi dev main.py
````

Accès au swagger sur http://127.0.0.1:8000/docs
accès au fichier Json http://127.0.0.1:8000/items/5?q=somequery avec (item_id=5 et q=somequery)