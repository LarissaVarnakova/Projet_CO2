# Analyse exploratoire et prétraitement des données pour la modélisation des émissions de CO₂ des véhicules commercialisés en France

## Projet Data Scientist — Liora (anciennement DataScientest)

**Formation :** Data Scientist – Liora (anciennement DataScientest)

**Projet :** Émissions de CO₂ des véhicules commercialisés en France

**Mentor :** Nicolas Mormiche

**Date :** Juin 2026

---

# Sommaire

1. Introduction

2. Contexte et objectifs
   - 2.1 Contexte
   - 2.2 Problématique
   - 2.3 Objectifs du projet

3. Présentation du jeu de données
   - 3.1 Origine des données
   - 3.2 Description du jeu de données
   - 3.3 Variable cible
   - 3.4 Synthèse

4. Analyse exploratoire des données
   - 4.1 Qualité des données
   - 4.2 Analyse descriptive
   - 4.3 Data visualisation
   - 4.4 Synthèse de l'analyse exploratoire

5. Data visualisation et analyses statistiques
   - 5.1 Corrélations
   - 5.2 Analyse de variance (ANOVA)
   - 5.3 Tests de Student
   - 5.4 Synthèse des analyses statistiques

6. Prétraitement des données
   - 6.1 Nettoyage des données
   - 6.2 Traitement des valeurs manquantes
   - 6.3 Feature Engineering
   - 6.4 Détection et traitement des valeurs aberrantes
   - 6.5 Encodage des variables catégorielles
   - 6.6 Préparation des données pour la modélisation
   - 6.7 Synthèse du prétraitement

7. Conclusion

8. Annexes

---

# 1. Introduction

La réduction des émissions de gaz à effet de serre constitue aujourd'hui un enjeu majeur pour le secteur des transports. En France, les véhicules particuliers et utilitaires représentent une part importante des émissions de dioxyde de carbone (CO₂), ce qui conduit les pouvoirs publics et les constructeurs automobiles à renforcer les politiques de réduction de l'impact environnemental des véhicules.

Dans ce contexte, l'analyse des données relatives aux caractéristiques techniques des véhicules permet de mieux comprendre les facteurs influençant les émissions de CO₂. L'identification de ces facteurs constitue une étape essentielle avant la mise en œuvre de modèles prédictifs capables d'estimer les émissions d'un véhicule à partir de ses caractéristiques.

Ce projet s'inscrit dans le cadre de la formation **Data Scientist** de **Liora (anciennement DataScientest)**. Il repose sur l'étude d'un jeu de données regroupant les caractéristiques techniques de véhicules commercialisés en France ainsi que leurs émissions de CO₂. L'objectif est de conduire une démarche complète d'analyse, d'exploration et de préparation des données en vue de leur exploitation par des modèles de Machine Learning.

Ce premier rapport présente les différentes étapes réalisées avant la phase de modélisation. Après une présentation du jeu de données, une analyse exploratoire est menée afin d'en comprendre la structure, d'identifier les principales relations entre les variables et de mettre en évidence les caractéristiques les plus influentes. Les opérations de prétraitement réalisées pour préparer les données à la modélisation sont ensuite détaillées et justifiées.

# 2. Contexte et objectifs

## 2.1 Contexte

La réduction des émissions de gaz à effet de serre constitue un enjeu environnemental majeur. En France, le secteur des transports représente une part importante des émissions de CO₂, les véhicules routiers contribuant significativement à cette empreinte carbone. Afin de limiter ces émissions, les pouvoirs publics mettent en œuvre des réglementations de plus en plus exigeantes, tandis que les constructeurs automobiles développent des motorisations plus performantes et moins polluantes.

Dans ce contexte, l'exploitation des données issues des véhicules commercialisés permet de mieux comprendre les facteurs influençant les émissions de CO₂. L'analyse de ces données constitue un levier essentiel pour accompagner les décisions des constructeurs, des organismes de réglementation et des acteurs engagés dans la transition écologique.

## 2.2 Problématique

Les émissions de CO₂ d'un véhicule dépendent de nombreux paramètres techniques, tels que la motorisation, la puissance, la masse, le type de carburant ou encore la consommation. Identifier les variables les plus influentes constitue une étape indispensable avant la mise en œuvre d'un modèle prédictif fiable.

La problématique retenue dans ce projet est donc la suivante :

> **Quels sont les principaux facteurs influençant les émissions de CO₂ des véhicules commercialisés en France, et comment préparer efficacement ces données en vue de leur modélisation ?**

## 2.3 Objectifs du projet

L'objectif principal de ce projet est de préparer un jeu de données fiable et exploitable pour une future phase de modélisation des émissions de CO₂.

Pour atteindre cet objectif, plusieurs étapes ont été réalisées :

- comprendre la structure du jeu de données ;
- évaluer la qualité des données et identifier les éventuelles anomalies ;
- analyser les relations entre les variables grâce à des méthodes statistiques et des visualisations adaptées ;
- mettre en œuvre un prétraitement rigoureux des données (traitement des valeurs manquantes, gestion des variables, encodage et préparation des jeux d'entraînement et de test) ;
- préparer un jeu de données directement exploitable par des modèles de Machine Learning.

### Synthèse du chapitre

Ce chapitre a permis de replacer le projet dans son contexte environnemental et d'en définir les principaux objectifs. La compréhension des facteurs influençant les émissions de CO₂ constitue le fil conducteur de cette étude. Les chapitres suivants présentent successivement le jeu de données utilisé, les analyses exploratoires réalisées ainsi que les différentes étapes de prétraitement mises en œuvre afin de préparer les données à la modélisation.

# 3. Présentation du jeu de données

## 3.1 Origine des données

Le jeu de données utilisé dans ce projet recense les caractéristiques techniques et environnementales des véhicules commercialisés en France en 2014. Il provient de données publiques diffusées par les autorités compétentes et rassemble des informations relatives aux émissions de CO₂, à la consommation de carburant, aux caractéristiques des motorisations ainsi qu'aux principaux polluants réglementés.

Ces données constituent une base pertinente pour analyser les facteurs susceptibles d'influencer les émissions de CO₂ des véhicules et préparer le développement de modèles prédictifs.

## 3.2 Description du jeu de données

Le jeu de données est composé d'observations correspondant à des véhicules commercialisés en France en 2014. Chaque ligne représente un véhicule et chaque colonne décrit une caractéristique technique ou environnementale.

Les variables couvrent notamment :

- les informations d'identification des véhicules ;
- les caractéristiques techniques (puissance, cylindrée, masse, type de carburant, transmission, etc.) ;
- les consommations de carburant ;
- les émissions de CO₂ ;
- les émissions des principaux polluants atmosphériques.

La variable cible retenue pour ce projet est **CO₂**, exprimée en grammes par kilomètre (g/km).

## 3.3 Variable cible

L'objectif de la future phase de modélisation sera de prédire les émissions de CO₂ d'un véhicule à partir de ses caractéristiques.

Cette variable quantitative constitue donc la variable cible de l'ensemble des analyses réalisées dans ce rapport. Les différentes étapes d'exploration et de prétraitement visent à identifier les variables les plus pertinentes et à préparer un jeu de données de qualité afin d'améliorer les performances des futurs modèles de Machine Learning.

## 3.4 Synthèse

Le jeu de données présente une richesse importante grâce à la diversité des informations techniques et environnementales disponibles pour chaque véhicule. Cette variété de variables permet d'étudier les principaux facteurs associés aux émissions de CO₂ tout en préparant un jeu de données adapté aux futures étapes de modélisation.

# 4. Analyse exploratoire des données

L'analyse exploratoire constitue une étape essentielle de tout projet de Data Science. Elle permet de comprendre la structure du jeu de données, d'évaluer sa qualité, d'identifier d'éventuelles anomalies et de mettre en évidence les premières relations entre les variables.

Cette phase conditionne l'ensemble des traitements réalisés par la suite. Elle permet notamment d'orienter les choix de prétraitement, de sélectionner les variables les plus pertinentes et de préparer les données en vue de leur future modélisation.

## 4.1 Qualité des données

La première étape de l'analyse exploratoire a consisté à examiner la structure générale du jeu de données afin d'en évaluer la qualité et la cohérence.

Le jeu de données est composé de **55 044 observations** décrites par **30 variables**. Il regroupe des informations relatives aux caractéristiques techniques des véhicules, à leur motorisation, à leur consommation de carburant ainsi qu'à leurs émissions de CO₂ et d'autres polluants réglementés.

L'examen des types de variables met en évidence une majorité de variables catégorielles (chaînes de caractères) décrivant notamment les marques, les modèles, les carburants ou les transmissions, ainsi que plusieurs variables numériques correspondant aux caractéristiques techniques et environnementales des véhicules.

L'analyse des valeurs manquantes révèle que la majorité des variables sont complètes. En revanche, certaines variables présentent un taux important de données manquantes. Les colonnes `Unnamed: 26` à `Unnamed: 29` sont entièrement vides (100 % de valeurs manquantes) et ne contiennent aucune information exploitable. La variable `date_maj` présente plus de **94 %** de valeurs manquantes, tandis que les variables `hc` et `hcnox` affichent respectivement environ **82 %** et **18 %** de données absentes.

À l'inverse, les variables directement liées à la problématique du projet présentent un très faible taux de valeurs manquantes. Les variables `ptcl`, `nox` et `co_typ_1`, qui seront conservées pour la suite des analyses, comportent moins de **5 %** de valeurs manquantes. Elles pourront donc être traitées lors de la phase de prétraitement sans dégrader significativement la qualité du jeu de données.

Cette première analyse confirme que le jeu de données est globalement de bonne qualité et qu'il est adapté à une démarche de modélisation après un prétraitement ciblé des variables concernées.

### Synthèse

L'analyse de la qualité des données met en évidence un jeu de données riche et globalement exploitable. Les principales difficultés concernent un nombre limité de variables fortement incomplètes, qui seront supprimées ou écartées de l'analyse. Les variables utiles à la modélisation présentent quant à elles très peu de valeurs manquantes, ce qui constitue un point favorable pour la suite du projet.

## 4.2 Analyse descriptive

Après avoir vérifié la qualité générale du jeu de données, une analyse descriptive a été réalisée afin de mieux comprendre les caractéristiques des véhicules étudiés.

L'examen des statistiques descriptives met en évidence une forte hétérogénéité des véhicules commercialisés en France en 2014. Les variables quantitatives, telles que la puissance du moteur, la cylindrée, la masse, la consommation de carburant ou encore les émissions de CO₂, présentent une dispersion importante, traduisant la diversité des modèles présents dans le jeu de données.

L'analyse de la variable cible montre que les émissions de CO₂ couvrent une plage de valeurs étendue, reflétant la coexistence de véhicules faiblement émetteurs et de véhicules plus énergivores. Cette variabilité constitue un point favorable pour la future phase de modélisation, puisqu'elle permettra aux modèles d'apprendre sur un ensemble représentatif de situations.

Les statistiques descriptives mettent également en évidence la présence de valeurs extrêmes pour certaines variables techniques. Une analyse spécifique des valeurs aberrantes sera réalisée lors de la phase de prétraitement afin de déterminer si ces observations correspondent à de véritables véhicules atypiques ou à d'éventuelles anomalies.

Enfin, l'analyse des variables catégorielles révèle une répartition déséquilibrée entre certaines modalités. Les motorisations essence et diesel sont largement majoritaires, tandis que les motorisations hybrides et électriques sont présentes en effectifs beaucoup plus faibles, ce qui est cohérent avec le marché automobile français en 2014.

### Synthèse

L'analyse descriptive met en évidence un jeu de données riche et varié, représentatif des véhicules commercialisés en France en 2014. La diversité des caractéristiques observées constitue un atout pour la modélisation, tout en justifiant la réalisation d'analyses statistiques et graphiques plus approfondies afin d'identifier les variables les plus influentes sur les émissions de CO₂.

## 4.3 Analyse graphique des données

Les visualisations réalisées au cours de l'analyse exploratoire ont permis de compléter les statistiques descriptives en mettant en évidence plusieurs relations importantes entre les caractéristiques techniques des véhicules et leurs émissions de CO₂.

L'étude de la distribution des émissions de CO₂ montre une forte variabilité des niveaux d'émission entre les véhicules commercialisés en France en 2014. Cette dispersion confirme l'intérêt de rechercher les variables les plus explicatives afin d'améliorer les performances des futurs modèles prédictifs.

Les analyses réalisées mettent en évidence une relation particulièrement marquée entre la consommation de carburant et les émissions de CO₂. Quel que soit le type de consommation étudié (urbaine, extra-urbaine ou mixte), une augmentation de la consommation s'accompagne d'une augmentation des émissions de CO₂. Cette relation constitue l'un des principaux résultats de l'analyse exploratoire.

Les graphiques montrent également que la puissance du moteur et la masse du véhicule influencent les émissions de CO₂. Les véhicules les plus lourds et les plus puissants présentent, dans l'ensemble, des émissions plus élevées, même si cette relation apparaît plus dispersée que celle observée avec la consommation.

L'étude des différents types de carburant met en évidence des différences significatives entre les motorisations. Les véhicules hybrides et électriques présentent globalement les niveaux d'émissions les plus faibles, tandis que les motorisations essence et diesel affichent des émissions plus élevées ainsi qu'une plus grande dispersion.

Enfin, l'analyse des corrélations confirme que les variables liées à la consommation de carburant figurent parmi les meilleurs indicateurs des émissions de CO₂. À l'inverse, certaines variables techniques présentent une influence beaucoup plus limitée et seront réévaluées lors de la phase de sélection des variables.

### Synthèse

Les analyses graphiques confirment que la consommation de carburant constitue le principal facteur associé aux émissions de CO₂. La puissance, la masse et le type de carburant contribuent également à expliquer une partie de la variabilité observée. Ces résultats orientent naturellement les choix réalisés lors de la phase de prétraitement et prépareront la sélection des variables utilisées pour la modélisation.

## 4.4 Synthèse de l'analyse exploratoire

L'analyse exploratoire a permis d'acquérir une compréhension approfondie du jeu de données et d'identifier les principaux facteurs susceptibles d'influencer les émissions de CO₂ des véhicules.

Le jeu de données présente une qualité globale satisfaisante. Les quelques valeurs manquantes observées concernent un nombre limité de variables d'intérêt et pourront être traitées sans perte significative d'information lors de la phase de prétraitement.

Les analyses descriptives et graphiques montrent que les émissions de CO₂ sont fortement liées à la consommation de carburant. La puissance du moteur, la masse du véhicule et le type de carburant apparaissent également comme des variables explicatives importantes, bien que leur influence soit moins marquée.

Les analyses statistiques réalisées confirment les observations issues des visualisations et mettent en évidence des relations significatives entre plusieurs variables explicatives et la variable cible. Elles permettent ainsi de conforter les choix qui seront réalisés lors du prétraitement et de la future phase de modélisation.

Cette analyse exploratoire constitue une étape essentielle du projet. Elle a permis de mettre en évidence les principales caractéristiques du jeu de données, d'identifier les variables les plus pertinentes et de définir une stratégie de prétraitement adaptée aux objectifs de modélisation des émissions de CO₂.