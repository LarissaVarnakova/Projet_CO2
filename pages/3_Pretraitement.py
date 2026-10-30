import streamlit as st

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Prétraitement — Projet CO₂",
    page_icon="⚙️",
    layout="wide"
)

# ============================================================
# INTRODUCTION
# ============================================================

st.title("⚙️ Prétraitement et Feature Engineering")

st.write(
    "Le prétraitement transforme les données brutes en données "
    "fiables, cohérentes et exploitables par les modèles "
    "de Machine Learning."
)

st.info(
    "Notre démarche : nettoyer les données, éviter les fuites "
    "d'information et sélectionner les variables pertinentes."
)

st.divider()

# ============================================================
# INDICATEURS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Observations initiales", "55 044")

with col2:
    st.metric("Observations conservées", "55 003")

with col3:
    st.metric("Variables explicatives finales", "93")

st.divider()

# ============================================================
# PIPELINE GLOBAL
# ============================================================

st.subheader("Notre pipeline de préparation")

st.markdown(
    """
    **55 044 observations brutes**

    ↓ Suppression de 7 doublons stricts

    **55 037 observations**

    ↓ Suppression de 34 observations sans CO₂

    **55 003 observations exploitables**

    ↓ Séparation Train / Test (80 % / 20 %)

    **44 002 observations d'entraînement — 11 001 observations de test**

    ↓ Imputation, Feature Engineering, sélection et encodage

    **93 variables explicatives finales**
    """
)

st.caption(
    "Les statistiques d'imputation et l'encodeur sont ajustés "
    "uniquement sur le jeu d'entraînement."
)

st.divider()

# ============================================================
# ONGLETS
# ============================================================

onglet1, onglet2, onglet3, onglet4 = st.tabs([
    "🧹 Nettoyage et séparation",
    "🔧 Imputation",
    "🧠 Feature Engineering",
    "🔢 Encodage et données finales"
])

# ============================================================
# ONGLET 1 — NETTOYAGE
# ============================================================

with onglet1:

    st.header("Nettoyage et séparation Train/Test")

    st.subheader("Nettoyage des observations")

    st.write(
        "Nous avons supprimé 7 doublons stricts, puis "
        "34 observations dont la variable cible CO₂ était manquante."
    )

    st.write(
        "Les véhicules présentant des caractéristiques techniques "
        "similaires ont été conservés lorsqu'aucune preuve "
        "de redondance stricte ne permettait de les supprimer."
    )

    st.warning(
        "Une caractéristique technique identique ne signifie pas "
        "nécessairement qu'il s'agit d'un doublon."
    )

    st.subheader("Séparation des données")

    col_train, col_test = st.columns(2)

    with col_train:
        st.metric("Entraînement — 80 %", "44 002")

    with col_test:
        st.metric("Test — 20 %", "11 001")

    st.success(
        "La séparation a été réalisée avant l'imputation "
        "et l'encodage pour éviter les fuites d'information."
    )

# ============================================================
# ONGLET 2 — IMPUTATION
# ============================================================

with onglet2:

    st.header("Traitement des valeurs manquantes")

    st.write(
        "Nous avons choisi une stratégie d'imputation "
        "adaptée à chaque variable, en utilisant exclusivement "
        "les statistiques du jeu d'entraînement."
    )

    st.table({
        "Variable": [
            "ptcl",
            "nox",
            "co_typ_1",
            "conso_mixte"
        ],
        "Méthode retenue": [
            "Médiane globale",
            "Médiane par carburant, sinon médiane globale",
            "Médiane par carburant, sinon médiane globale",
            "Médiane globale"
        ]
    })

    st.write(
        "Pour les variables nox et co_typ_1, les différences "
        "observées entre les motorisations justifient "
        "une imputation conditionnelle selon le carburant."
    )

    st.info(
        "Les médianes sont calculées sur X_train, "
        "puis appliquées à X_train et X_test."
    )

    st.success(
        "Après imputation, aucune valeur manquante ne subsiste "
        "sur ces quatre variables."
    )

# ============================================================
# ONGLET 3 — FEATURE ENGINEERING
# ============================================================

with onglet3:

    st.header("Feature Engineering et sélection des variables")

    st.subheader("Création de variables")

    st.write(
        "Deux ratios puissance/masse ont été étudiés "
        "pour représenter la puissance du véhicule "
        "relativement à sa masse."
    )

    st.latex(
        r"\text{rapport\_puissance\_masse}"
        r"=\frac{\text{puiss\_max}}{\text{masse\_ordma\_min}}"
    )

    st.table({
        "Variable": [
            "rapport_puissance_masse",
            "rapport_puissance_masse_max"
        ],
        "Corrélation avec le CO₂": [
            "≈ 0,089",
            "≈ 0,054"
        ],
        "Décision": [
            "Conservée",
            "Supprimée"
        ]
    })

    st.write(
        "Les deux ratios sont très fortement corrélés "
        "entre eux (≈ 0,985). Nous avons conservé "
        "le rapport utilisant la masse minimale "
        "afin de limiter la redondance."
    )

    st.divider()

    st.subheader("Sélection des variables")

    col_gauche, col_droite = st.columns(2)

    with col_gauche:
        st.markdown("**Variables écartées**")
        st.write(
            "puiss_admin_98, conso_urb, conso_exurb, "
            "champ_v9, cnit, tvv, dscom, lib_mod et lib_mod_doss."
        )

    with col_droite:
        st.markdown("**Variables importantes conservées**")
        st.write(
            "conso_mixte, puiss_max, masse_ordma_min, "
            "masse_ordma_max et les variables catégorielles "
            "retenues pour l'encodage."
        )

    st.info(
        "Les valeurs extrêmes ont été étudiées, mais "
        "conservées lorsqu'aucune erreur n'était démontrée."
    )

# ============================================================
# ONGLET 4 — ENCODAGE ET DONNÉES FINALES
# ============================================================

with onglet4:

    st.header("Encodage et préparation des données finales")

    st.subheader("Encodage One-Hot")

    st.write(
        "Six variables catégorielles ont été transformées "
        "avec OneHotEncoder de scikit-learn."
    )

    st.markdown(
        """
        - `lib_mrq` : marque
        - `cod_cbr` : carburant
        - `hybride` : hybridation
        - `Carrosserie` : carrosserie
        - `gamme` : gamme du véhicule
        - `typ_boite_nb_rapp` : boîte de vitesses
        """
    )

    st.code(
        'OneHotEncoder(drop="first", handle_unknown="ignore")',
        language="python"
    )

    st.write(
        "L'encodeur est ajusté uniquement sur le jeu "
        "d'entraînement, puis appliqué au jeu de test."
    )

    st.divider()

    st.subheader("Standardisation")

    st.write(
        "La standardisation a été évaluée pour les modèles "
        "sensibles à l'échelle des variables, notamment "
        "la régression linéaire, Ridge, Lasso et le MLP."
    )

    st.write(
        "Elle n'a pas été appliquée systématiquement "
        "aux modèles fondés sur les arbres."
    )

    st.divider()

    st.subheader("Dimensions finales")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("X_train", "44 002 × 93")

    with col2:
        st.metric("X_test", "11 001 × 93")

    st.success(
        "Les données finales sont numériques, complètes "
        "et prêtes pour la modélisation."
    )
