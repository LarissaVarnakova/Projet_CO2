import streamlit as st
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Modélisation — Projet CO₂",
    page_icon="🤖",
    layout="wide"
)

RACINE_PROJET = Path(__file__).resolve().parent.parent
DOSSIER_FIGURES = RACINE_PROJET / "reports" / "figures"


def afficher_figure(nom_fichier, legende, largeur=750):
    chemin = DOSSIER_FIGURES / nom_fichier

    if chemin.exists():
        st.image(str(chemin), width=largeur)
        st.caption(legende)
    else:
        st.warning(f"Figure introuvable : {nom_fichier}")


# ============================================================
# INTRODUCTION
# ============================================================

st.title("🤖 Modélisation des émissions de CO₂")

st.write(
    "Nous avons comparé plusieurs familles d'algorithmes "
    "afin de prédire les émissions de CO₂ des véhicules "
    "à partir de leurs caractéristiques techniques."
)

st.info(
    "Notre démarche : partir d'un modèle de référence, "
    "augmenter progressivement la complexité et vérifier "
    "les performances sur des données indépendantes."
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Observations d'entraînement", "44 002")

with col2:
    st.metric("Observations de test", "11 001")

with col3:
    st.metric("Variables explicatives", "93")

st.divider()


# ============================================================
# ONGLETS
# ============================================================

onglet1, onglet2, onglet3, onglet4 = st.tabs([
    "🎯 Démarche",
    "🧩 Modèles étudiés",
    "🔍 Optimisation",
    "🧪 Expérimentations"
])


# ============================================================
# ONGLET 1 — DÉMARCHE
# ============================================================

with onglet1:

    st.header("Notre protocole de modélisation")

    st.write(
        "Tous les modèles de l'étude principale sont évalués "
        "sur le même jeu de test, afin de permettre "
        "une comparaison cohérente."
    )

    st.subheader("Indicateurs d'évaluation")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**MAE — Erreur absolue moyenne**")
        st.write(
            "Mesure l'écart absolu moyen entre les émissions "
            "réelles et prédites, en g/km."
        )

        st.markdown("**RMSE — Racine de l'erreur quadratique moyenne**")
        st.write(
            "Pénalise davantage les erreurs importantes. "
            "Elle s'exprime également en g/km."
        )

    with col_b:
        st.markdown("**R² — Coefficient de détermination**")
        st.write(
            "Mesure la qualité de l'ajustement du modèle "
            "par rapport à une prédiction fondée sur la moyenne."
        )

        st.markdown("**MAPE — Erreur absolue moyenne en pourcentage**")
        st.write(
            "Mesure l'erreur relative moyenne. "
            "Dans notre rapport, elle est exprimée sous forme "
            "de proportion : 0,0017 correspond à 0,17 %."
        )

    st.divider()

    st.subheader("Une progression méthodologique")

    st.markdown(
        """
        **DummyRegressor**
        
        ↓ Établir une référence minimale

        **Régression linéaire, Ridge et Lasso**

        ↓ Tester les relations linéaires et la régularisation

        **Arbre de décision**

        ↓ Introduire des relations non linéaires

        **Random Forest**

        ↓ Réduire la variance par bagging

        **XGBoost et LightGBM**

        ↓ Explorer les méthodes de boosting

        **MLP**

        ↓ Tester une architecture neuronale
        """
    )

    st.success(
        "Chaque nouvelle famille de modèles répond à "
        "une hypothèse de modélisation identifiable."
    )


# ============================================================
# ONGLET 2 — MODÈLES ÉTUDIÉS
# ============================================================

with onglet2:

    st.header("Les familles de modèles évaluées")

    with st.expander("1. DummyRegressor — Modèle de référence"):
        st.write(
            "Le DummyRegressor prédit systématiquement "
            "la moyenne des émissions de CO₂. "
            "Il permet de mesurer l'amélioration apportée "
            "par les modèles supervisés."
        )
        st.metric("MAE de référence", "22,45 g/km")

    with st.expander("2. Régression linéaire, Ridge et Lasso"):
        st.write(
            "La régression linéaire teste une relation additive "
            "entre les variables explicatives et le CO₂."
        )
        st.write(
            "Ridge utilise une pénalisation L2 et Lasso "
            "une pénalisation L1. Dans notre étude, "
            "la régularisation n'apporte pas de gain "
            "prédictif notable par rapport à la régression linéaire."
        )

    with st.expander("3. Arbre de décision"):
        st.write(
            "L'arbre de décision utilise des seuils successifs "
            "pour représenter des relations non linéaires "
            "et des interactions entre les caractéristiques."
        )

    with st.expander("4. Random Forest"):
        st.write(
            "Random Forest combine plusieurs arbres "
            "afin de réduire la sensibilité aux variations "
            "des données d'entraînement."
        )
        st.write(
            "Le modèle optimisé utilise 100 arbres, "
            "une profondeur maximale de 20, "
            "min_samples_split=2 et min_samples_leaf=1."
        )

    with st.expander("5. XGBoost et LightGBM"):
        st.write(
            "Ces deux algorithmes reposent sur le gradient boosting. "
            "Ils construisent successivement des arbres "
            "pour améliorer les prédictions."
        )
        st.write(
            "Notre configuration XGBoost initiale comprend "
            "100 arbres, une profondeur maximale de 6 "
            "et un taux d'apprentissage de 0,1."
        )

    with st.expander("6. Réseau de neurones MLP"):
        st.write(
            "Nous avons également expérimenté un réseau "
            "de neurones à deux couches cachées de "
            "64 et 32 neurones, avec activation ReLU."
        )
        st.write(
            "Le réseau utilise Adam, une perte MSE, "
            "100 epochs et des lots de 32 observations."
        )
        st.metric("Paramètres du réseau", "8 129")


# ============================================================
# ONGLET 3 — OPTIMISATION
# ============================================================

with onglet3:

    st.header("Optimisation et validation croisée")

    st.subheader("Recherche d'hyperparamètres")

    st.write(
        "Nous avons utilisé GridSearchCV pour comparer "
        "différentes configurations, avec une validation "
        "croisée à cinq plis et le R² comme critère de sélection."
    )

    st.markdown(
        """
        **Principe :**

        - Diviser le jeu d'entraînement en cinq plis.
        - Ajuster le modèle sur quatre plis.
        - Évaluer la configuration sur le cinquième.
        - Répéter l'opération pour chaque pli.
        - Comparer les scores moyens de validation.
        """
    )

    st.info(
        "Le jeu de test reste indépendant de la recherche "
        "d'hyperparamètres."
    )

    st.divider()

    st.subheader("Exemple : optimisation de XGBoost")

    st.table({
        "Hyperparamètre": [
            "n_estimators",
            "learning_rate",
            "max_depth"
        ],
        "Valeurs explorées": [
            "100, 200",
            "0,05 ; 0,1",
            "4, 6, 8"
        ]
    })

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Configurations", "12")

    with col2:
        st.metric("Ajustements CV", "60")

    st.write(
        "La meilleure configuration de la grille "
        "comprend 200 arbres, une profondeur de 4 "
        "et un taux d'apprentissage de 0,1."
    )

    st.warning(
        "L'optimisation n'a pas amélioré le RMSE sur le jeu "
        "de test : environ 0,71 g/km après recherche, "
        "contre 0,5940 g/km pour le modèle initial."
    )

    st.divider()

    st.subheader("Courbes d'apprentissage")

    modele_courbe = st.selectbox(
        "Choisir un modèle",
        ["Random Forest", "XGBoost", "LightGBM"]
    )

    figures_apprentissage = {
        "Random Forest": (
            "random_forest_apprentissage.png",
            "Courbe d'apprentissage Random Forest — validation croisée à trois plis."
        ),
        "XGBoost": (
            "xgboost_apprentissage.png",
            "Courbe d'apprentissage XGBoost — validation croisée à cinq plis."
        ),
        "LightGBM": (
            "lightgbm_apprentissage.png",
            "Courbe d'apprentissage LightGBM — validation croisée à cinq plis."
        )
    }

    fichier, legende = figures_apprentissage[modele_courbe]

    afficher_figure(fichier, legende, largeur=750)

    st.write(
        "Les courbes permettent de comparer les scores "
        "d'entraînement et de validation lorsque "
        "la quantité de données augmente."
    )


# ============================================================
# ONGLET 4 — EXPÉRIMENTATIONS
# ============================================================

with onglet4:

    st.header("Expérimentations complémentaires")

    experience = st.selectbox(
        "Choisir une expérimentation",
        [
            "Standardisation du MLP",
            "Suppression de la consommation mixte",
            "Target Encoding"
        ]
    )

    if experience == "Standardisation du MLP":

        st.subheader("Effet de la standardisation sur le MLP")

        st.write(
            "Nous avons comparé deux réseaux identiques "
            "avec les mêmes poids initiaux et les mêmes "
            "paramètres d'entraînement. "
            "Seule la standardisation des variables change."
        )

        st.table({
            "Configuration": [
                "Sans standardisation",
                "Avec standardisation"
            ],
            "MAE (g/km)": [
                "9,1259",
                "0,7971"
            ],
            "RMSE (g/km)": [
                "9,3855",
                "1,3355"
            ],
            "R²": [
                "0,9245",
                "0,9985"
            ]
        })

        st.success(
            "Dans cette expérimentation contrôlée, "
            "la standardisation réduit la MAE d'environ 91 %."
        )

        st.caption(
            "Cette expérience utilise un protocole distinct "
            "de celui du MLP du notebook principal."
        )

    elif experience == "Suppression de la consommation mixte":

        st.subheader("Prédire sans la variable conso_mixte")

        st.write(
            "Nous avons supprimé conso_mixte pour mesurer "
            "la dépendance des modèles à cette variable."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Variables initiales", "93")

        with col2:
            st.metric("Variables sans conso_mixte", "92")

        st.table({
            "Modèle": [
                "Random Forest",
                "XGBoost"
            ],
            "RMSE sans conso_mixte": [
                "4,82 g/km",
                "4,82 g/km"
            ],
            "R² sans conso_mixte": [
                "0,9801",
                "0,9801"
            ]
        })

        st.write(
            "Les performances se dégradent après suppression "
            "de la consommation mixte, mais Random Forest "
            "et XGBoost conservent un R² de 0,9801."
        )

        st.info(
            "Cette expérimentation ouvre une perspective : "
            "estimer les émissions d'un véhicule lorsque "
            "sa consommation mixte n'est pas connue."
        )

    elif experience == "Target Encoding":

        st.subheader("Target Encoding versus One-Hot Encoding")

        st.write(
            "Nous avons évalué le Target Encoding avec "
            "une approche out-of-fold à cinq plis "
            "afin de limiter les fuites d'information."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("One-Hot Encoding", "93 variables")

        with col2:
            st.metric("Target Encoding", "13 variables")

        st.write(
            "Dans les pipelines étudiés, la dimension "
            "passe de 93 à 13 variables, soit environ "
            "86 % de réduction."
        )

        st.table({
            "Modèle": [
                "Régression linéaire",
                "Ridge",
                "Lasso",
                "Arbre de décision"
            ],
            "R² One-Hot": [
                "0,9974",
                "0,9974",
                "0,9923",
                "0,9991"
            ],
            "R² Target Encoding": [
                "0,9837",
                "0,9829",
                "0,9808",
                "0,9986"
            ]
        })

        st.warning(
            "Les pipelines ne sont pas strictement identiques. "
            "La réduction de dimension et les écarts de performance "
            "ne peuvent donc pas être attribués uniquement "
            "au choix de l'encodage."
        )

        st.success(
            "Perspective : comparer les deux encodages "
            "à variables et protocoles identiques."
        )
