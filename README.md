# Prédiction des émissions de CO₂ des véhicules commercialisés en France

## Sommaire

- [ 1. Présentation du projet](#1-présentation-du-projet) 
- [ 2. Organisation du dépôt Git](#2-organisation-du-dépôt-git) 
- [ 3. Installation de l'environnement](#3-installation-de-lenvironnement) 
- [ 4. Notebooks du projet](#4-notebooks-du-projet) 
- [ 5. Modèles étudiés](#5-modèles-étudiés) 
- [ 6. Application Streamlit](#6-application-streamlit) 
- [ 7. Vérification de la reproductibilité](#7-vérification-de-la-reproductibilité) 
- [ 8. Rapport et documentation](#8-rapport-et-documentation) 
- [ 9. Auteurs](#9-auteurs) 


## 1. Présentation du projet

Ce projet a été réalisé dans le cadre de la formation Data Scientist – Liora (anciennement DataScientest).

L'objectif est d'analyser les caractéristiques techniques et environnementales des véhicules commercialisés en France en 2014, puis de construire des modèles de régression capables de prédire leurs émissions de CO₂, exprimées en g/km.

### 1.2. Équipe projet :

- **Larissa Varnakova**
- **Aziz Diallo**
- **Mentor : Nicolas Mormiche**

### 1.3. Vue d'ensemble de pipeline méthodologique du projet
- **1. Collecte des données :**  
    - Source - ADEME / data.gouv.fr — véhicules commercialisés en France en 2014 [co2_2014.csv](data/co2_2014.csv)  contenant 55 044 observations et 30 variables.
- **2. Nettoyage initial :**  
    - Suppression de 7 doublons stricts, des 34 lignes sans cible CO₂ et des colonnes inutilisables;  
    - 55 003 observations conservées.  
- **3. Analyse exploratoire (EDA) :**  
    - Qualité des données, distributions, visualisations, corrélations et tests statistiques;  
    - Identification des variables associées aux émissions de CO₂.  
- **4. Séparation des données :**  
    - Train : 44 002 observations ;  
    - Test : 11 001 observations  ;  
    - Proportions 80 % / 20 % — avant imputation et encodage.
- **5. Prétraitement et feature engineering :**  
    - Imputation des valeurs manquantes;  
    - Analyse des valeurs extrêmes;  
    - Sélection des variables et encodage `One-Hot`;
    - Transformations ajustées sur Train - [X_train_final.csv](data/X_train_final.csv), puis appliquées à Test - [X_test_final.csv](data/X_test_final.csv). 
- **6. Modélisation supervisée :** <a id="modeles"></a>
    - DummyRegressor;  
    - Régressions linéaires;  
    - Ridge et Lasso;  
    - Arbres de décision;  
    - Random Forest;  
    - XGBoost;  
    - LightGBM;  
    - MLP.
- **7. Évaluation et comparaison :**
    - MAE · RMSE · R² · MAPE;  
    - Validation croisée, recherche d'hyperparamètres et analyse des erreurs.
- **8. Modèle de référence : XGBoost**
    - R² = 0,9997 · RMSE = 0,5940 g/km sur le jeu de test.
- **9. Interprétabilité et conclusion :**
    - Analyse SHAP, identification des variables influentes et discussion des limites du modèle.



## 2. Organisation du dépôt Git

```text

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
````

Le dossier `data/` contient les données initiales et les jeux préparés.  
Le dossier `models/` regroupe les objets nécessaires à la prédiction.  
Les `notebooks` retracent les différentes étapes de l'analyse et de la modélisation.  
Le dossier `reports/` contient le rapport du projet et les figures utilisées pour présenter les résultats.  

## 3. Installation de l'environnement

### 3.1. Prérequis

- `Python 3.12.10` - [Télécharger sur le site officiel de Python](https://www.python.org/downloads/release/python-31210/). 
    - aller jusqu'à la section **Files** 
    - choisir l'installateur en fonction de votre système d'exploitation 

- `Git` - [Télécharger Git](https://git-scm.com/downloads)
- `Terminal` - déjà intégré à macOS et Linux. Sous Windows, utiliser PowerShell ou Windows Terminal.
- un environnement permettant d'exécuter des notebooks Jupyter, au choix:
    - `Visual Studio Code` - [Téléchargement officiel](https://code.visualstudio.com/download). Il faudra ensuite installer les extensions Python et Jupyter.
    - `Anaconda Distribution` - [Téléchargement officiel](https://www.anaconda.com/download). Cette distribution comprend Python, Jupyter Notebook, JupyterLab et des outils de gestion des environnements.


### 3.2 Installation 


**3.2.1. Cloner le projet depuis Git**

- Ouvrir un terminal depuis l'endroit souhaité et récupérer le projet depuis Git :
 
```bash
git clone --branch main https://github.com/LarissaVarnakova/Projet_CO2.git
```
**3.2.2. Ouverture dans Visual Studio Code**
- Ouvrir Visual Studio Code:  
    - Sous macOS dans terminal :   
    ```bash
    code .
    ``` 
    - Sous Windows dans Power Shell :  
    ```bash
    cd Projet_CO2
    code .
    ````

- Si vous preferez lancez VSCode depuis L'environnement Windows,séléctionnez **Fichier → Ouvrir le dossier** et choisissez le dossier contenant le projet cloné.  
- Ouvrir un terminal intégré dans VSCode: **Terminal → Nouveau terminal**.

**3.2.3. Configurer l'environnement virtuel du projet `venv_CO2`**
- Dans le terminal intégré de VS Code, exécuter les commandes suivantes :  
```bash
python3 --version
``` 
Verifier que la version est bien 3.12.XX sinon revenez sur l’étape d'installation de Python et installez la bonne version ( 3.12.10). 
- Pour macOS/Linux :
```bash 
python3.12 -m venv .venv_CO2 
``` 
- pour Windows :
```bash 
py 3.12 -m venv .venv_CO2 
``` 
- Activer l'environnement virtuel:  
    - sur macOS/Linux :  
    ```bash
    source .venv_CO2/bin/activate
    ```
    - Sur Windows (PowerShell) :  
    ```bash
    .venv_CO2\Scripts\Activate.ps1
    ```
    - Sur Windows (Invite de commandes / CMD) :  
    ```bash
    .venv_CO2\Scripts\activate.bat
    ```
Une fois l’environnement activé, le nom (.venv_CO2) apparaît généralement au début de la ligne de commande dans terminal de VSCode.  

**3.2.4. Installation des dépendances**  

- Mettre à jour pip, puis installer les bibliothèques nécessaires au projet :  
    ```bash
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```   
- vérifier la cohérence des dépendances installées :  
    ```bash
    python -m pip check
    ```  

**3.2.5. Installation des extensions**  

Cliquer sur l’icône **Extensions** dans la barre latérale gauche ( ou appuyer sur `Ctrl + Shift + X`):  
- Installer l’extension `Python`, publiée par `Microsoft`;  
- Installer l’extension `Jupyter`.  
- Installer ipykernel :  
    ```bash
    python -m pip install ipykernel
    ```
- Installer IpProgress ( barre de progression pour Notebook) :  
    ```bash
    python -m pip install ipywidgets
    ```
  
    
**3.2.6. Sélection de l’interpréteur Python dans VS Code** 
- Ouvrir la palette de commandes : `Cmd + Shift + P` sur macOS ou `Ctrl + Shift + P` sur Windows.  
- Rechercher *Python* 
- Sélectionner l’interpréteur de l’environnement `.venv_CO2` :  
    
    - macOS / Linux : `.venv_CO2/bin/`;  
    
    - Windows : `.venv_CO2\Scripts\python.exe`.  

*Si l’interpréteur n’apparaît pas dans la liste, sélectionner manuellement le chemin correspondant.*

Arrivé à ce stade, vous pouvez passer à l'execution des notebooks.


## 4. Notebooks du projet

Les notebooks se trouvent dans le dossier `notebooks/`.  
Ils sont organisés selon les différentes étapes du projet :

- Analyse exploratoire, distributions, corrélations et tests statistiques - [eda.ipynb](notebooks/eda.ipynb) 
- Nettoyage, imputation, création de variables, encodage et préparation des jeux de données - [preprocessing.ipynb](notebooks/preprocessing.ipynb) 
- Entraînement, optimisation et comparaison des modèles de régression - [modelisation.ipynb](notebooks/modelisation.ipynb) 
- Étude de l'effet de la standardisation sur certains modèles - [experimentation_scaling.ipynb](notebooks/experimentation_scaling.ipynb)  
- Expérimentation d'un encodage alternatif des variables catégorielles - [modelisation_target_encoding.ipynb](notebooks/modelisation_target_encoding.ipynb) 
- Étude des performances sans la variable conso_mixte - [experience_sans_conso_mixte.ipynb](notebooks/experience_sans_conso_mixte.ipynb)  
- Exploration des modèles avec LazyPredict - [lazypredict.ipynb](notebooks/lazypredict.ipynb)

Ordre de lecture conseillé :  
- eda.ipynb
- preprocessing.ipynb
- modelisation.ipynb 
- les trois notebooks d'expérimentation, selon l'analyse souhaitée 
- exploration automatique avecLazyPredict. 


Les notebooks utilisent principalement des chemins relatifs vers les dossiers `data/` et `models/`.

**Important : pour que les chemins de type `../data/` fonctionnent, les notebooks doivent être exécutés avec le dossier `notebooks/` comme répertoire de travail.**

Les fichiers de données préparées et les modèles sauvegardés sont également fournis dans le dépôt. Il n'est donc pas nécessaire de relancer tous les entraînements pour utiliser l'application Streamlit.

## 5. Modèles étudiés

Plusieurs approches de régression ont été comparées - voir [Modélisation supervisée](#modeles).

Les performances ont été évaluées à l'aide des métriques MAE, RMSE, R² et MAPE.

Principaux résultats

| Modèle        | MAE    | RMSE   | R²     |
|---------------|------:|-------:|-------:|
| LightGBM      | 0,3701 | 1,2902 | 0,9986 |
| Random Forest | 0,0925 | 0,7112 | 0,9996 |
| XGBoost       | 0,2908 | 0,5940 | 0,9997 |

XGBoost a été retenu pour l'application Streamlit en raison de ses performances globales, notamment sur la RMSE.

Random Forest obtient toutefois la meilleure MAE parmi les modèles comparés.

Ces résultats sont détaillés dans le rapport du projet.

## 6. Application Streamlit

Une application Streamlit permet d'estimer les émissions de CO₂ d'un véhicule à partir de ses caractéristiques techniques choisies.

Elle utilise :

- `models/preprocessing_co2.joblib` pour les paramètres de prétraitement et l'encodage ;

- `models/xgboost_co2.json` pour le modèle XGBoost entraîné.

**6.1 Comment lancer l'application Streamlit** 

Depuis la racine du projet, avec l'environnement virtuel activé :  
```bash
python -m streamlit run app.py
```
L'application est généralement accessible à l'adresse : [streamlit](http://localhost:8501)

L'utilisateur renseigne les caractéristiques du véhicule, puis lance la prédiction.
Le résultat est affiché en grammes de CO₂ par kilomètre (g/km).

## 7. Vérification de la reproductibilité

Un test de reproductibilité a été réalisé sur:
- la machine virtuelle Windows;
- mac mini 4.

Les vérifications suivantes ont été effectuées avec succès :

- Clonage du dépôt depuis GitHub ;  
- Création d'un environnement virtuel indépendant avec Python 3.12.10 ;  
- Installation des dépendances depuis requirements.txt ;  
- Vérification des dépendances avec pip check ;  
- Importation des principales bibliothèques Python ;  
- Chargement du prétraitement et du modèle XGBoost sauvegardés ;  
- Vérification des 93 variables attendues par le modèle ;  
- Prédictions sur les 11 001 observations du jeu de test ;  
- Démarrage de l'application Streamlit ;  
- Réalisation d'une prédiction depuis l'interface.

Les performances obtenues après rechargement du modèle XGBoost sont :

| Métrique | Résultat |
|----------|---------:|
| MAE      | 0,2908   |
| RMSE     | 0,5940   |
| R²       | 0,9997   |


Ces résultats correspondent à ceux présentés dans le rapport.
**Périmètre de validation :** ces tests confirment la reconstruction de l'environnement, l'exécution intégrale de tous les notebooks depuis leur première cellule, le fonctionnement du modèle sauvegardé et l'utilisation de l'application Streamlit. 

## 8. Rapport et documentation

Le rapport principal est disponible dans le dossier `reports/`, au format Markdown et PDF.

Il présente :

- Le contexte et les objectifs du projet ;
- L'analyse exploratoire et les résultats statistiques ;
- Les choix de prétraitement ;
- La méthodologie de modélisation ;
- La comparaison et l'interprétation des performances ;
- Les limites et les perspectives d'évolution.
- Les graphiques associés sont regroupés dans reports/figures/.

## 9. Auteurs

Larissa Varnakova et Aziz Diallo

Projet réalisé dans le cadre de la formation Data Scientist – Liora (anciennement DataScientest), sous l'accompagnement de Nicolas Mormiche.

Octobre 2026.
