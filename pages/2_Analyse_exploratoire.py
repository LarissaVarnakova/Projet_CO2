import streamlit as st
from pathlib import Path


# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="Analyse exploratoire — Projet CO₂",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CHEMIN DES FIGURES
# ============================================================

RACINE_PROJET = Path(__file__).resolve().parent.parent
DOSSIER_FIGURES = RACINE_PROJET / "reports" / "figures"


# ============================================================
# FONCTION D'AFFICHAGE DES FIGURES
# ============================================================

def afficher_figure(nom_fichier, legende, largeur=750):
    chemin = DOSSIER_FIGURES / nom_fichier

    if chemin.exists():
        st.image(
            str(chemin),
            width=largeur
        )
        st.caption(legende)
    else:
        st.warning(f"Figure introuvable : {nom_fichier}")


# ============================================================
# INTRODUCTION
# ============================================================

st.title("📊 Analyse exploratoire des données (EDA)")

st.write(
    "L'analyse exploratoire permet de comprendre les données, "
    "d'évaluer leur qualité et d'identifier les relations "
    "entre les caractéristiques des véhicules et leurs émissions de CO₂."
)

st.info(
    "Notre objectif : identifier les facteurs associés aux émissions "
    "de CO₂ afin d'orienter le prétraitement et la modélisation."
)

st.divider()


# ============================================================
# ONGLETS
# ============================================================

onglet1, onglet2, onglet3, onglet4 = st.tabs([
    "🔎 Qualité des données",
    "📈 Analyse descriptive",
    "📉 Corrélations et statistiques",
    "💡 Synthèse"
])


# ============================================================
# ONGLET 1 — QUALITÉ DES DONNÉES
# ============================================================

with onglet1:

    st.header("Qualité du jeu de données")

    st.write(
        "Le jeu de données initial contient 55 044 observations "
        "et 30 variables. L'analyse des valeurs manquantes "
        "a permis d'identifier plusieurs anomalies."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Observations initiales", "55 044")

    with col2:
        st.metric("Variables initiales", "30")

    with col3:
        st.metric("Colonnes entièrement vides", "4")

    st.subheader("Principales valeurs manquantes")

    st.table({
        "Variable": [
            "Unnamed: 26 à 29",
            "date_maj",
            "hc",
            "hcnox",
            "ptcl, nox, co_typ_1"
        ],
        "Valeurs manquantes": [
            "100 %",
            "Plus de 94 %",
            "Environ 82 %",
            "Environ 18 %",
            "Moins de 5 %"
        ]
    })

    st.write(
        "La majorité des variables sont suffisamment complètes "
        "pour poursuivre l'analyse. Les colonnes très incomplètes "
        "ou non informatives seront traitées lors du prétraitement."
    )

    st.success(
        "Enseignement : un nettoyage ciblé est nécessaire "
        "avant l'entraînement des modèles."
    )


# ============================================================
# ONGLET 2 — ANALYSE DESCRIPTIVE
# ============================================================

with onglet2:

    st.header("Distribution et caractéristiques des véhicules")

    st.subheader("1. Distribution des émissions de CO₂")

    afficher_figure(
        "image.png",
        "Figure 1 — Distribution des émissions de CO₂."
    )

    st.write(
        "Les émissions présentent une dispersion importante, "
        "ce qui traduit la diversité des véhicules étudiés."
    )

    st.divider()

    st.subheader("2. Consommation mixte et émissions de CO₂")

    afficher_figure(
        "image-1.png",
        "Figure 2 — Relation entre la consommation mixte et les émissions de CO₂."
    )

    st.write(
        "La consommation mixte présente une relation positive "
        "très marquée avec les émissions de CO₂. "
        "Plus la consommation augmente, plus les émissions "
        "ont tendance à augmenter."
    )

    st.info(
        "Cette observation a orienté notre choix de conserver "
        "la consommation mixte pour la modélisation."
    )

    st.divider()

    st.subheader("3. Émissions selon le type de carburant")

    afficher_figure(
        "image-5.png",
        "Figure 3 — Distribution des émissions de CO₂ selon le carburant."
    )

    st.write(
        "Les émissions varient selon les motorisations. "
        "Les véhicules essence et diesel présentent une dispersion "
        "plus importante, tandis que les véhicules hybrides "
        "affichent globalement des niveaux d'émissions plus faibles."
    )


# ============================================================
# ONGLET 3 — CORRÉLATIONS ET STATISTIQUES
# ============================================================

with onglet3:

    st.header("Corrélations et analyses statistiques")

    st.subheader("1. Corrélations entre les variables numériques")

    afficher_figure(
        "image-3.png",
        "Figure 4 — Matrice de corrélation des variables numériques.",
        largeur=850
    )

    st.write(
        "Les variables liées à la consommation de carburant "
        "présentent les associations les plus fortes avec le CO₂. "
        "La masse du véhicule présente également une relation positive."
    )

    st.caption(
        "Une corrélation ne constitue pas une preuve de causalité."
    )

    st.divider()

    st.subheader("2. Corrélations entre les consommations")

    afficher_figure(
        "correlations_consommations.png",
        "Figure 5 — Corrélations entre consommations urbaine, "
        "extra-urbaine et mixte, calculées sur le jeu d'entraînement.",
        largeur=500
    )

    st.write(
        "Les différentes mesures de consommation sont fortement "
        "corrélées entre elles. Cette redondance a orienté "
        "la sélection des variables lors du prétraitement."
    )

    st.divider()

    st.subheader("3. Tests statistiques")

    with st.expander("ANOVA — Comparaison des catégories", expanded=True):

        st.write(
            "Les analyses de variance montrent des différences "
            "statistiquement significatives d'émissions de CO₂ "
            "selon le type de carburant, la carrosserie "
            "et la gamme du véhicule."
        )

    with st.expander("Test de Student — Hybridation", expanded=True):

        afficher_figure(
            "image-6.png",
            "Figure 6 — Distribution des émissions de CO₂ selon l'hybridation."
        )

        st.write(
            "Le test de Student met en évidence une différence "
            "statistiquement significative entre véhicules "
            "hybrides et non hybrides. Les véhicules hybrides "
            "présentent globalement des émissions plus faibles."
        )


# ============================================================
# ONGLET 4 — SYNTHÈSE
# ============================================================

with onglet4:

    st.header("Les principaux enseignements de l'EDA")

    st.write(
        "L'exploration et les analyses statistiques nous ont permis "
        "d'identifier les variables pertinentes et les traitements "
        "nécessaires avant la modélisation."
    )

    st.markdown(
        """
        **1. Qualité des données**

        Certaines variables sont entièrement vides ou fortement
        incomplètes : un nettoyage est nécessaire.

        **2. Consommation de carburant**

        La consommation mixte est fortement associée aux émissions
        de CO₂ et constitue une variable importante pour la prédiction.

        **3. Caractéristiques techniques**

        La masse et certaines caractéristiques des véhicules
        sont associées aux niveaux d'émissions.

        **4. Variables catégorielles**

        Le carburant, la carrosserie, la gamme et l'hybridation
        présentent des différences significatives d'émissions.
        """
    )

    st.success(
        "Conclusion : les résultats de l'EDA ont directement "
        "guidé nos choix de nettoyage, de sélection des variables "
        "et de préparation des données pour le Machine Learning."
    )
