# Projet-5BDDD

Projet du cours 5BDDD (création des API et BDD)
Utilisation de _FastAPI_

Lien documentation : https://fastapi.tiangolo.com/virtual-environments/ ou https://docs.python.org/3/library/venv.html

## installation Linux

```bash
python3 -m venv venv
source venv/bin/activate

## Installation des librairies listées dans requirements.txt
pip install -r requirements.txt
pip freeze
````

Désactivation de l'environnement virtuel
```bash
deactivate
````

## Démarrage de l'application main.py
 
Variable d'environnement à definir 
```test
TEST=1475955669
BDD_url=sqlite://:memory:
```

```bash
fastapi dev main.py
````

Accès au swagger sur http://127.0.0.1:8000/docs
accès au fichier Json http://127.0.0.1:8000/items/5?q=somequery avec (item_id=5 et q=somequery)
Accès à la page index.html http://127.0.0.1:8000/static/index.html