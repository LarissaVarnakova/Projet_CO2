import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Jeu de données — Projet CO₂",
    page_icon="📂",
    layout="wide"
)


# ============================================================
# CHEMIN DES DONNÉES
# ============================================================

RACINE_PROJET = Path(__file__).resolve().parent.parent
CHEMIN_DONNEES = RACINE_PROJET / "data" / "co2_2014.csv"


# ============================================================
# CHARGEMENT DES DONNÉES
# ============================================================

@st.cache_data
def charger_donnees():
    return pd.read_csv(
        CHEMIN_DONNEES,
        encoding="cp1252",
        sep=None,
        engine="python"
    )


df = charger_donnees()

# ============================================================
# TITRE
# ============================================================

st.title("📂 Présentation du jeu de données")

st.write(
    "Cette partie présente les données utilisées dans notre projet "
    "de prédiction des émissions de CO₂ des véhicules "
    "commercialisés en France."
)

st.divider()


# ============================================================
# ORIGINE DES DONNÉES
# ============================================================

st.header("🌍 Origine des données")

st.write(
    "Les données proviennent de l'ADEME et sont publiées "
    "sur la plateforme data.gouv.fr. Elles concernent les "
    "véhicules commercialisés en France en 2014."
)

st.write(
    "L'ADEME acquiert ces informations auprès de l'UTAC, "
    "organisme chargé de l'homologation des véhicules "
    "avant leur commercialisation."
)

st.divider()


# ============================================================
# CHIFFRES CLÉS
# ============================================================

st.header("📊 Le jeu de données en quelques chiffres")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Année",
        "2014"
    )

with col2:
    st.metric(
        "Observations initiales",
        f"{len(df):,}".replace(",", " ")
    )

with col3:
    st.metric(
        "Nombre de variables initiales",
        df.shape[1]
    )

st.caption(
    "Après nettoyage, le jeu de données contient "
    "55 003 observations. Les étapes de nettoyage seront "
    "détaillées dans la partie Prétraitement."
)

st.divider()


# ============================================================
# STRUCTURE DES DONNÉES
# ============================================================

st.header("🔎 Structure du jeu de données")

st.write(
    "Chaque ligne correspond à un véhicule et chaque colonne "
    "décrit une caractéristique technique ou environnementale."
)

with st.expander("Afficher un aperçu des données", expanded=True):

    colonnes_selectionnees = st.multiselect(
        "Sélectionnez les variables à afficher",
        options=df.columns.tolist(),
        default=df.columns[:8].tolist()
    )

    nombre_lignes = st.slider(
        "Nombre de lignes",
        min_value=5,
        max_value=30,
        value=10,
        step=5
    )

    if colonnes_selectionnees:
        st.dataframe(
            df[colonnes_selectionnees].head(nombre_lignes),
            use_container_width=True
        )
    else:
        st.warning(
            "Sélectionnez au moins une variable."
        )

st.divider()


# ============================================================
# VARIABLE CIBLE
# ============================================================

st.header("🎯 Notre variable cible")

st.metric(
    label="Variable à prédire",
    value="CO₂ (g/km)"
)

st.write(
    "Notre objectif est de prédire les émissions de CO₂ "
    "d'un véhicule à partir de ses caractéristiques techniques "
    "et environnementales."
)

st.divider()


# ============================================================
# VARIABLES EXPLICATIVES
# ============================================================

st.header("⚙️ Les variables explicatives")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):
        st.subheader("🚘 Caractéristiques techniques")
        st.write(
            "Puissance, masse, cylindrée et type de transmission."
        )

    with st.container(border=True):
        st.subheader("⛽ Motorisation et consommation")
        st.write(
            "Type de carburant, hybridation et consommation "
            "de carburant."
        )

with col2:

    with st.container(border=True):
        st.subheader("🌱 Données environnementales")
        st.write(
            "Émissions des principaux polluants atmosphériques."
        )

    with st.container(border=True):
        st.subheader("🏷️ Identification du véhicule")
        st.write(
            "Marque, modèle et références techniques."
        )

st.divider()


# ============================================================
# SYNTHÈSE
# ============================================================

st.header("💡 À retenir")

st.success(
    "Le jeu de données ADEME 2014 regroupe des informations "
    "techniques et environnementales permettant d'étudier "
    "les facteurs associés aux émissions de CO₂ et de "
    "construire des modèles prédictifs."
)
