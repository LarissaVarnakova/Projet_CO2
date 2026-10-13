Prédiction des émissions de CO₂ des véhicules commercialisés en France

1. Présentation du projet

Ce projet a été réalisé dans le cadre de la formation Data Scientist – Liora (anciennement DataScientest).

L'objectif est d'analyser les caractéristiques techniques et environnementales des véhicules commercialisés en France en 2014, puis de construire des modèles de régression capables de prédire leurs émissions de CO₂, exprimées en g/km.

Équipe projet :

Larissa Varnakova

Aziz Diallo

Mentor : Nicolas Mormiche

Le projet couvre l'analyse exploratoire des données, leur préparation, l'entraînement et la comparaison de plusieurs modèles de Machine Learning, ainsi que le développement d'une application Streamlit permettant d'effectuer des prédictions.

2. Données utilisées

Le fichier initial co2_2014.csv contient 55 044 observations et 30 variables.

Après suppression de 7 doublons stricts et de 34 observations sans valeur cible co2, le jeu de données utilisé pour la modélisation comprend 55 003 observations.

La répartition est la suivante :

Jeu de données

Observations

Entraînement

44 002

Test

11 001

Les données sont préparées à partir des caractéristiques des véhicules : marque, motorisation, carburant, puissance, consommation, masse, carrosserie, gamme et boîte de vitesses.

Le prétraitement comprend notamment le traitement des valeurs manquantes, la création de variables, la sélection des caractéristiques et l'encodage des variables catégorielles.

Le jeu de données final comporte 93 variables explicatives après encodage.

3. Organisation du dépôt

Projet_CO2/
│
├── data/
│   ├── co2_2014.csv
│   ├── X_train_final.csv
│   ├── X_test_final.csv
│   ├── y_train.csv
│   └── y_test.csv
│
├── models/
│   ├── preprocessing_co2.joblib
│   └── xgboost_co2.json
│
├── notebooks/
│   ├── eda.ipynb
│   ├── preprocessing.ipynb
│   ├── modelisation.ipynb
│   ├── experimentation_scaling.ipynb
│   ├── modelisation_target_encoding.ipynb
│   └── experience_sans_conso_mixte.ipynb
│
├── reports/
│   ├── figures/
│   ├── rapport_CO2.md
│   ├── rapport_rendu1.md
│   └── Prédiction des émissions de CO₂ des véhicules commercialisés en France.pdf
│
├── references/
├── src/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

Le dossier data/ contient les données initiales et les jeux préparés. Le dossier models/ regroupe les objets nécessaires à la prédiction. Les notebooks retracent les différentes étapes de l'analyse et de la modélisation.

Le dossier reports/ contient le rapport du projet et les figures utilisées pour présenter les résultats.

4. Installation de l'environnement

Prérequis

Python 3.12

Git

Un terminal

Un environnement permettant d'exécuter des notebooks Jupyter

L'installation a été testée sous Linux avec Python 3.12.3.

Récupérer le projet

git clone --branch aziz-eda https://github.com/LarissaVarnakova/Projet_CO2.git
cd Projet_CO2

Créer un environnement virtuel

Sous Linux :

python3 -m venv venv
source venv/bin/activate

Sous Windows (PowerShell) :

python -m venv venv
.\venv\Scripts\Activate.ps1

Installer les dépendances

python -m pip install -r requirements.txt

Pour vérifier la cohérence des dépendances installées :

python -m pip check

Le fichier requirements.txt contient les bibliothèques nécessaires à l'analyse, à la modélisation et à l'application, notamment pandas, NumPy, scikit-learn, XGBoost, LightGBM, TensorFlow, SHAP et Streamlit.

5. Notebooks du projet

Les notebooks se trouvent dans le dossier notebooks/.

Ils sont organisés selon les différentes étapes du projet :

Notebook

Contenu

eda.ipynb

Analyse exploratoire, distributions, corrélations et tests statistiques

preprocessing.ipynb

Nettoyage, imputation, création de variables, encodage et préparation des jeux de données

modelisation.ipynb

Entraînement, optimisation et comparaison des modèles de régression

experimentation_scaling.ipynb

Étude de l'effet de la standardisation sur certains modèles

modelisation_target_encoding.ipynb

Expérimentation d'un encodage alternatif des variables catégorielles

experience_sans_conso_mixte.ipynb

Étude des performances sans la variable conso_mixte

Ordre de lecture conseillé

eda.ipynb

preprocessing.ipynb

modelisation.ipynb

Les trois notebooks d'expérimentation, selon l'analyse souhaitée.

Les notebooks utilisent principalement des chemins relatifs vers les dossiers data/ et models/.

Important : pour que les chemins de type ../data/ fonctionnent, les notebooks doivent être exécutés avec le dossier notebooks/ comme répertoire de travail.

Les fichiers de données préparées et les modèles sauvegardés sont également fournis dans le dépôt. Il n'est donc pas nécessaire de relancer tous les entraînements pour utiliser l'application Streamlit.

6. Modèles étudiés

Plusieurs approches de régression ont été comparées :

Dummy Regressor, comme modèle de référence ;

Régression linéaire, Ridge et Lasso ;

Arbre de décision ;

Random Forest ;

XGBoost ;

LightGBM ;

Réseau de neurones multicouche (MLP).

Les performances sont évaluées à l'aide des métriques MAE, RMSE, R² et MAPE.

Principaux résultats

Modèle

MAE (g/km)

RMSE (g/km)

R²

XGBoost

0,2908

0,5940

0,9997

Random Forest

0,0925

0,7112

0,9996

LightGBM

0,3701

1,2902

0,9986

XGBoost a été retenu pour l'application Streamlit en raison de ses performances globales, notamment sur la RMSE.

Random Forest obtient toutefois la meilleure MAE parmi les modèles comparés.

Ces résultats sont détaillés dans le rapport du projet.

7. Application Streamlit

Une application Streamlit permet d'estimer les émissions de CO₂ d'un véhicule à partir de ses caractéristiques techniques.

Elle utilise :

models/preprocessing_co2.joblib pour les paramètres de prétraitement et l'encodage ;

models/xgboost_co2.json pour le modèle XGBoost entraîné.

Lancer l'application

Depuis la racine du projet, avec l'environnement virtuel activé :

python -m streamlit run app.py

L'application est généralement accessible à l'adresse :

http://localhost:8501

L'utilisateur renseigne les caractéristiques du véhicule, puis lance la prédiction.

Le résultat est affiché en grammes de CO₂ par kilomètre (g/km).

8. Vérification de la reproductibilité

Un test de reproductibilité a été réalisé sur un serveur Linux, à partir d'un nouveau clonage de la branche aziz-eda.

Les vérifications suivantes ont été effectuées avec succès :

Clonage du dépôt depuis GitHub ;

Création d'un environnement virtuel indépendant avec Python 3.12.3 ;

Installation des dépendances depuis requirements.txt ;

Vérification des dépendances avec pip check ;

Importation des principales bibliothèques Python ;

Chargement du prétraitement et du modèle XGBoost sauvegardés ;

Vérification des 93 variables attendues par le modèle ;

Prédictions sur les 11 001 observations du jeu de test ;

Démarrage de l'application Streamlit ;

Réalisation d'une prédiction depuis l'interface.

Les performances obtenues après rechargement du modèle XGBoost sont :

Métrique

Résultat

MAE

0,2908

RMSE

0,5940

R²

0,9997

Ces résultats correspondent à ceux présentés dans le rapport.

Périmètre de validation : ces tests confirment la reconstruction de l'environnement, le fonctionnement du modèle sauvegardé et l'utilisation de l'application. Ils ne constituent pas encore une validation de l'exécution intégrale de tous les notebooks depuis leur première cellule.

9. Rapport et documentation

Le rapport principal est disponible dans le dossier reports/, au format Markdown et PDF.

Il présente :

Le contexte et les objectifs du projet ;

L'analyse exploratoire et les résultats statistiques ;

Les choix de prétraitement ;

La méthodologie de modélisation ;

La comparaison et l'interprétation des performances ;

Les limites et les perspectives d'évolution.

Les graphiques associés sont regroupés dans reports/figures/.

10. Auteurs

Larissa Varnakova et Aziz Diallo

Projet réalisé dans le cadre de la formation Data Scientist – Liora (anciennement DataScientest), sous l'accompagnement de Nicolas Mormiche.

Octobre 2026.
