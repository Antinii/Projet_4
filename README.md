# Projet 4 OpenClassrooms
## Développer un programme logiciel en utilisant Python

Cette application est un programme autonome et hors ligne permettant la gestion de tournois d'echecs.

Vous pouvez à l'aide de ce programme, gérer les points suivants:
- ajouter des joueurs dans la base de données
- ajouter des tournois dans la base de données
- lancer un tournoi
- renseigner le vainqueur d'un match
- afficher une liste des joueurs par ordre alphabétique
- afficher une liste des tournois 
- afficher les joueurs d'un tournoi spécifique
- afficher les tours et matchs d'un tournoi spécifique avec un leaderboard


### Installation:
Vous devez avoir préalablement Python 3.11 installé ainsi qu'un IDE (PyCharm ou Virtual Studio)

Placez vous dans le répertoire souhaité puis clonez le repository:
```
git clone https://github.com/Antinii/Projet_4.git
```
Déplacez vous dans le dossier du repository avec:
```
cd '.\Projet_4\'
```
Créez votre environnement virtuel:
```
python -m venv env
```
Activez votre environnement virtuel:
```
env\Scripts\activate (pour windows)
ou
source env/bin/activate (pour linux)
```
Installez les packages nécessaires:
```
pip install -r requirements.txt
```
Et pour terminer, lancez le script:
```
python main.py
```
À l'aide du menu principal vous choisissez les différentes options qui s'offrent à vous.
Afin de générer un nouveau rapport flake8:
```
flake8 --format=html --htmldir=flake8_rapport
```