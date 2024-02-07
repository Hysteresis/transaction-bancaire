# Transaction Bancaire App

Cette application permet de visualiser et d'analyser 
les transactions bancaires ficitves à partir d'une base de données Oracle.

## Dépendances

- **Python 3.10+**
- **tkinter**
- **matplotlib** : `pip install matplotlib`
- **oracledb** `pip install oracledb`

## Installation

1. Assurez-vous que Python 3.10+ est installé sur votre système.
2. Installez les dépendances ci-dessus
3. Clonez ce dépôt : ``git clone https://github.com/Hysteresis/transaction-bancaire.git``
4. Accédez au répertoire du projet : ``cd transaction-bancaire``
5. Lancez l'application en exécutant le fichier `main.py` :


## Utilisation

Une fois l'application lancée, vous verrez une interface graphique avec plusieurs boutons. 

Voici ce que chaque bouton fait :

- "**Grosse catégorie de dépense**" : Affiche la plus grosse catégorie de dépense avec son montant total.
- "**Sous catégorie de revenu**" : Affiche la plus grosse sous-catégorie de source de revenu avec son montant total.
- "**Évolution du solde**" : Affiche un graphique montrant l'évolution du solde client à travers le temps.

la **base de données** avec des valeurs fictives n'est pas en ligne et s'installe en **localhost**.

## Auteur

Ce projet a été créé par Pierre MARBOUTIN le 07/02/24.



