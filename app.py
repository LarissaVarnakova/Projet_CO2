import streamlit as st
import pandas as pd
import joblib
from xgboost import XGBRegressor


# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="Prédiction des émissions de CO₂",
    page_icon="🚗",
    layout="wide"
)


# ============================================================
# CHARGEMENT DU MODÈLE ET DU PREPROCESSING
# ============================================================

@st.cache_resource
def charger_modele():
    preprocessing = joblib.load("models/preprocessing_co2.joblib")

    model = XGBRegressor()
    model.load_model("models/xgboost_co2.json")

    return model, preprocessing


model, preprocessing = charger_modele()

# ============================================================
# CATÉGORIES APPRISES PAR L'ENCODEUR
# ============================================================

categories = {
    variable: list(cats)
    for variable, cats in zip(
        preprocessing["variables_a_encoder"],
        preprocessing["encoder"].categories_
    )
}


# ============================================================
# LIBELLÉS D'AFFICHAGE
# ============================================================

def afficher_boite(code):
    correspondances = {
        "A": "Automatique",
        "M": "Manuelle",
        "D": "Double embrayage",
        "S": "Séquentielle",
        "V": "Variation continue"
    }

    parties = str(code).split()

    if len(parties) == 2:
        type_boite, rapports = parties

        libelle = correspondances.get(type_boite, type_boite)

        if rapports.isdigit() and rapports != "0":
            return f"{libelle} – {rapports} rapports"

        return libelle

    return str(code)

# ============================================================
# EN-TÊTE
# ============================================================

st.title("🚗 Prédiction des émissions de CO₂")

st.write(
    "Cette application estime les émissions de CO₂ d'un véhicule "
    "à partir de ses caractéristiques techniques."
)

st.info(
    "Renseignez les caractéristiques du véhicule, puis cliquez sur "
    "« Prédire les émissions de CO₂ »."
)

st.divider()


# ============================================================
# FORMULAIRE
# ============================================================

with st.form("formulaire_prediction"):

    # --------------------------------------------------------
    # CARACTÉRISTIQUES GÉNÉRALES
    # --------------------------------------------------------

    st.subheader("🚘 Caractéristiques générales")

    col1, col2 = st.columns(2)

    with col1:

        lib_mrq = st.selectbox(
            "Marque",
            categories["lib_mrq"]
        )

        hybride = st.selectbox(
            "Motorisation hybride",
            categories["hybride"]
        )

        gamme = st.selectbox(
            "Gamme",
            categories["gamme"]
        )

    with col2:

        cod_cbr = st.selectbox(
            "Carburant (code)",
            categories["cod_cbr"],
            help="Codification du carburant issue du jeu de données d'origine."
        )

        Carrosserie = st.selectbox(
            "Carrosserie",
            categories["Carrosserie"]
        )

        typ_boite_nb_rapp = st.selectbox(
            "Boîte de vitesses",
            categories["typ_boite_nb_rapp"],
            format_func=afficher_boite
        )


    st.divider()


    # --------------------------------------------------------
    # CARACTÉRISTIQUES TECHNIQUES
    # --------------------------------------------------------

    st.subheader("⚙️ Caractéristiques techniques")

    col3, col4, col5 = st.columns(3)

    with col3:

        puiss_max = st.number_input(
            "Puissance maximale (kW)",
            min_value=28.0,
            max_value=585.0,
            value=120.0,
            step=1.0
        )

    with col4:

        masse_ordma_min = st.number_input(
            "Masse minimale (kg)",
            min_value=825.0,
            max_value=2760.0,
            value=2076.0,
            step=1.0
        )

    with col5:

        masse_ordma_max = st.number_input(
            "Masse maximale (kg)",
            min_value=825.0,
            max_value=3094.0,
            value=2355.0,
            step=1.0
        )


    st.divider()


    # --------------------------------------------------------
    # DONNÉES ENVIRONNEMENTALES
    # --------------------------------------------------------

    st.subheader("🌱 Données environnementales")

    col6, col7 = st.columns(2)

    with col6:

        conso_mixte = st.number_input(
            "Consommation mixte (L/100 km)",
            min_value=0.0,
            max_value=24.5,
            value=7.8,
            step=0.1
        )

        nox = st.number_input(
            "NOx (g/km)",
            min_value=0.0,
            max_value=1.846,
            value=0.214,
            step=0.001,
            format="%.3f"
        )

    with col7:

        co_typ_1 = st.number_input(
            "CO – essai type I (g/km)",
            min_value=0.005,
            max_value=6.968,
            value=0.137,
            step=0.001,
            format="%.3f"
        )

        ptcl = st.number_input(
            "Particules (g/km)",
            min_value=0.0,
            max_value=0.023,
            value=0.001,
            step=0.001,
            format="%.3f"
        )


    st.write("")

    bouton_prediction = st.form_submit_button(
        "🚗 Prédire les émissions de CO₂",
        type="primary",
        use_container_width=True
    )


# ============================================================
# PRÉDICTION
# ============================================================

if bouton_prediction:

    # Vérification de cohérence des masses
    if masse_ordma_min > masse_ordma_max:

        st.error(
            "La masse minimale ne peut pas être supérieure "
            "à la masse maximale."
        )

    else:

        # Création de l'observation
        nouvelle_observation = pd.DataFrame({
            "puiss_max": [puiss_max],
            "conso_mixte": [conso_mixte],
            "co_typ_1": [co_typ_1],
            "nox": [nox],
            "ptcl": [ptcl],
            "masse_ordma_min": [masse_ordma_min],
            "masse_ordma_max": [masse_ordma_max],
            "lib_mrq": [lib_mrq],
            "cod_cbr": [cod_cbr],
            "hybride": [hybride],
            "Carrosserie": [Carrosserie],
            "gamme": [gamme],
            "typ_boite_nb_rapp": [typ_boite_nb_rapp]
        })


        # ----------------------------------------------------
        # ENCODAGE
        # ----------------------------------------------------

        variables_cat = preprocessing["variables_a_encoder"]

        donnees_encodees = preprocessing["encoder"].transform(
            nouvelle_observation[variables_cat]
        )

        noms_colonnes_encodees = (
            preprocessing["encoder"]
            .get_feature_names_out(variables_cat)
        )

        df_encode = pd.DataFrame(
            donnees_encodees,
            columns=noms_colonnes_encodees
        )


        # ----------------------------------------------------
        # VARIABLES NUMÉRIQUES
        # ----------------------------------------------------

        variables_numeriques = [
            "puiss_max",
            "conso_mixte",
            "co_typ_1",
            "nox",
            "ptcl",
            "masse_ordma_min",
            "masse_ordma_max"
        ]

        df_numerique = nouvelle_observation[
            variables_numeriques
        ].reset_index(drop=True)


        # ----------------------------------------------------
        # ASSEMBLAGE DES 91 VARIABLES
        # ----------------------------------------------------

        donnees_finales = pd.concat(
            [df_numerique, df_encode],
            axis=1
        )

        donnees_finales = donnees_finales.reindex(
            columns=preprocessing["colonnes_finales"],
            fill_value=0
        )


        # ----------------------------------------------------
        # PRÉDICTION XGBOOST
        # ----------------------------------------------------

        prediction = float(
            model.predict(donnees_finales)[0]
        )


        # ----------------------------------------------------
        # AFFICHAGE DU RÉSULTAT
        # ----------------------------------------------------

        st.divider()

        st.subheader("📊 Résultat de la prédiction")

        st.metric(
            label="Émissions de CO₂ estimées",
            value=f"{prediction:.1f} g/km"
        )

        st.caption(
            "Estimation produite par le modèle XGBoost entraîné "
            "dans le cadre du projet."
        )




        # ============================================================
# LIBELLÉS D'AFFICHAGE
# ============================================================

def afficher_boite(code):
    correspondances = {
        "A": "Automatique",
        "M": "Manuelle",
        "D": "Double embrayage",
        "S": "Séquentielle",
        "V": "Variation continue"
    }

    parties = str(code).split()

    if len(parties) == 2:
        type_boite, rapports = parties

        libelle = correspondances.get(type_boite, type_boite)

        if rapports.isdigit() and rapports != "0":
            return f"{libelle} – {rapports} rapports"

        return libelle

    return str(code)