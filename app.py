import streamlit as st


# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="Projet CO₂ — Soutenance DataScientest",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# EN-TÊTE
# ============================================================

st.title(
    "🚗 Prédiction des émissions de CO₂ "
    "des véhicules commercialisés en France"
)

st.subheader(
    "Analyse des données ADEME 2014 et modélisation "
    "par Machine Learning"
)

st.write("**Projet Data Scientist — Liora (anciennement DataScientest)**")

st.write("**Réalisé par :** Larissa Varnakova et Aziz Diallo")
st.write("**Mentor :** Nicolas Mormiche")
st.write("**Date :** Octobre 2026")

st.divider()


# ============================================================
# PROBLÉMATIQUE
# ============================================================

st.header("🎯 Notre problématique")

st.info(
    "Quels sont les principaux facteurs influençant les émissions "
    "de CO₂ des véhicules commercialisés en France et comment "
    "exploiter ces informations pour construire un modèle de "
    "Machine Learning capable de prédire ces émissions ?"
)

st.divider()


# ============================================================
# OBJECTIFS ET DÉMARCHE
# ============================================================

st.header("🔎 Notre démarche")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):
        st.subheader("📊 Comprendre les données")
        st.write(
            "Explorer les caractéristiques techniques et "
            "environnementales des véhicules."
        )

    with st.container(border=True):
        st.subheader("🧹 Préparer les données")
        st.write(
            "Nettoyer les données, traiter les valeurs manquantes "
            "et préparer les variables pour la modélisation."
        )

with col2:

    with st.container(border=True):
        st.subheader("🔍 Identifier les facteurs")
        st.write(
            "Analyser les relations entre les caractéristiques "
            "des véhicules et leurs émissions de CO₂."
        )

    with st.container(border=True):
        st.subheader("🤖 Prédire les émissions")
        st.write(
            "Entraîner, comparer et interpréter plusieurs modèles "
            "de régression."
        )

st.divider()


# ============================================================
# CHIFFRES CLÉS
# ============================================================

st.header("📌 Le projet en quelques chiffres")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Année des données",
        value="2014"
    )

with col2:
    st.metric(
        label="Observations finales",
        value="55 003"
    )

with col3:
    st.metric(
        label="Variables après encodage",
        value="93"
    )

st.divider()


# ============================================================
# PRÉSENTATION DU PARCOURS
# ============================================================

st.header("🧭 Le parcours de notre soutenance")

st.write(
    "À travers les différentes rubriques de cette application, "
    "nous présenterons notre démarche complète de Data Science : "
    "de l'exploration des données jusqu'à la prédiction "
    "interactive des émissions de CO₂."
)

st.success(
    "Utilisez le menu latéral pour naviguer dans notre projet."
)
