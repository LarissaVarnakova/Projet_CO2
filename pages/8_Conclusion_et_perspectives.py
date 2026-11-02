import streamlit as st

st.set_page_config(
    page_title="Conclusion et perspectives",
    page_icon="🎯",
    layout="wide"
)

# --------------------------------------------------
# EN-TÊTE
# --------------------------------------------------

st.title("🎯 Conclusion et perspectives")

st.write(
    "Notre projet a permis d'explorer, préparer, modéliser et "
    "interpréter les émissions de CO₂ des véhicules "
    "commercialisés en France en 2014."
)

st.info(
    "Notre enseignement principal : un modèle performant doit "
    "aussi être évalué en fonction des données réellement "
    "disponibles au moment de son utilisation."
)

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Observations étudiées", "55 003")
col2.metric("RMSE XGBoost", "0,5940 g/km")
col3.metric("R² XGBoost", "0,9997")

st.divider()

# --------------------------------------------------
# ONGLETS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs([
    "🏆 Bilan du projet",
    "⚠️ Difficultés et limites",
    "🚀 Perspectives d'évolution"
])

# --------------------------------------------------
# ONGLET 1 : BILAN
# --------------------------------------------------

with tab1:

    st.header("Bilan général du projet")

    st.subheader("Une démarche complète de Data Science")

    st.markdown("""
    Notre travail a couvert les principales étapes d'un projet
    de Machine Learning :

    1. Analyse exploratoire des données ADEME/UTAC.
    2. Contrôle de qualité et analyse des doublons.
    3. Prétraitement sans utilisation des statistiques du jeu de test.
    4. Comparaison de plusieurs familles d'algorithmes.
    5. Optimisation et évaluation des modèles.
    6. Interprétation des prédictions avec SHAP.
    7. Développement d'un simulateur interactif.
    """)

    st.divider()

    st.subheader("Les principaux résultats")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**XGBoost — Modèle principal**")
        st.metric("RMSE", "0,5940 g/km")
        st.metric("R²", "0,9997")

        st.write(
            "XGBoost a été retenu en privilégiant la réduction "
            "des erreurs importantes, mesurées par le RMSE."
        )

    with col2:
        st.markdown("**Random Forest — Meilleure MAE**")
        st.metric("MAE", "0,0925 g/km")

        st.write(
            "Random Forest minimise l'erreur absolue moyenne. "
            "Le choix du meilleur modèle dépend donc de la "
            "métrique privilégiée."
        )

    st.success(
        "Les modèles d'ensemble ont obtenu les meilleures "
        "performances de notre comparaison, avec XGBoost "
        "retenu comme modèle principal."
    )

    st.divider()

    st.subheader("Ce que nous avons appris")

    st.markdown("""
    - Les modèles non linéaires améliorent les performances
      sur ce jeu de données.
    - La préparation des données et le choix de l'encodage
      influencent les résultats.
    - La standardisation améliore fortement le MLP dans
      notre expérimentation contrôlée.
    - SHAP confirme le rôle prédominant de la consommation mixte.
    - Les performances doivent être interprétées selon les
      conditions réelles d'utilisation.
    """)

# --------------------------------------------------
# ONGLET 2 : DIFFICULTÉS ET LIMITES
# --------------------------------------------------

with tab2:

    st.header("Difficultés rencontrées et limites")

    st.subheader("1. Ressources de calcul")

    st.write(
        "Les recherches d'hyperparamètres, les validations "
        "croisées et l'entraînement du MLP ont nécessité "
        "du temps de calcul. L'absence ou l'indisponibilité "
        "d'une accélération GPU dans certains environnements "
        "a ralenti les expérimentations."
    )

    st.subheader("2. Collaboration et environnement")

    st.write(
        "Le travail en binôme a demandé une coordination "
        "des notebooks, des dépendances Python, des fichiers "
        "de données et des branches Git."
    )

    st.divider()

    st.subheader("3. Dépendance à la consommation mixte")

    st.warning(
        "La variable conso_mixte est très fortement liée "
        "aux émissions de CO₂. Sa disponibilité lors "
        "d'une utilisation réelle du modèle est déterminante."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Modèle XGBoost avec conso_mixte**")
        st.metric("RMSE", "0,5940 g/km")
        st.metric("R²", "0,9997")

    with col2:
        st.markdown("**Expérimentation sans conso_mixte**")
        st.metric("RMSE", "4,82 g/km")
        st.metric("R²", "0,9801")

    st.info(
        "La suppression de conso_mixte dégrade les performances, "
        "mais montre que d'autres caractéristiques techniques "
        "conservent un potentiel prédictif important."
    )

    st.divider()

    st.subheader("4. Généralisation des résultats")

    st.write(
        "Les résultats ont été obtenus sur des véhicules "
        "commercialisés en France en 2014. Ils ne démontrent "
        "pas automatiquement une généralisation à d'autres "
        "années, à de nouveaux protocoles d'homologation "
        "ou aux véhicules électriques."
    )

# --------------------------------------------------
# ONGLET 3 : PERSPECTIVES
# --------------------------------------------------

with tab3:

    st.header("Nos perspectives d'évolution")

    st.write(
        "Cinq axes d'amélioration ont été identifiés "
        "à partir des résultats et des limites de notre étude."
    )

    st.divider()

    st.subheader(
        "🚗 1. Prédire les émissions avant commercialisation"
    )

    st.write(
        "Développer un modèle capable d'estimer les émissions "
        "de CO₂ d'un véhicule encore en phase de conception, "
        "à partir de caractéristiques techniques disponibles "
        "en amont : puissance, masse, carburant ou hybridation."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Variables explicatives après encodage, sans conso_mixte", "92")
    col2.metric("R² obtenu", "0,9801")
    col3.metric("RMSE obtenu", "4,82 g/km")

    st.success(
        "L'expérimentation sans consommation mixte constitue "
        "une première étape vers la prédiction des émissions "
        "de véhicules non encore commercialisés."
    )

    st.caption(
        "Cette perspective nécessite une validation sur "
        "de nouveaux véhicules et une vérification des "
        "variables disponibles en phase de conception."
    )

    st.divider()

    with st.expander(
        "🧩 2. Approfondir le Target Encoding",
        expanded=False
    ):

        col1, col2 = st.columns(2)

        col1.metric("One-Hot Encoding", "93 variables")
        col2.metric("Target Encoding", "13 variables")

        st.write(
            "Le Target Encoding réduit fortement la dimension "
            "des données, mais les quatre modèles évalués "
            "ont obtenu des performances inférieures à celles "
            "du One-Hot Encoding."
        )

        st.info(
            "Perspective : comparer les deux approches avec "
            "des variables et des protocoles identiques, "
            "en étudiant la précision, le temps de calcul "
            "et la stabilité."
        )

    with st.expander(
        "🧠 3. Améliorer le MLP et son optimisation",
        expanded=False
    ):

        st.write(
            "Poursuivre les essais avec différentes architectures, "
            "EarlyStopping, Dropout ou une optimisation bayésienne, "
            "tout en conservant un protocole comparable "
            "et un budget de calcul explicite."
        )

    with st.expander(
        "📅 4. Tester la généralisation temporelle",
        expanded=False
    ):

        st.write(
            "Évaluer les modèles sur des données d'autres années, "
            "après harmonisation des schémas, afin de mesurer "
            "leur robustesse sur des véhicules plus récents."
        )

        st.write(
            "Renforcer également la documentation et "
            "la reproductibilité du pipeline."
        )

    with st.expander(
        "🔎 5. Approfondir l'analyse des doublons",
        expanded=False
    ):

        col1, col2 = st.columns(2)

        col1.metric("Doublons stricts supprimés", "7")
        col2.metric(
            "Groupes techniquement similaires",
            "4 388"
        )

        st.write(
            "Les groupes de véhicules techniquement similaires "
            "ont été conservés, faute de preuve qu'il s'agisse "
            "de doublons réels."
        )

        st.write(
            "Une étude complémentaire pourrait comparer "
            "différentes stratégies de traitement des doublons "
            "et mesurer leur influence sur les performances "
            "et la généralisation des modèles."
        )

    st.divider()

    st.subheader("Notre message final")

    st.success(
        "La qualité d'un projet de Data Science ne repose pas "
        "uniquement sur ses scores prédictifs, mais aussi sur "
        "la rigueur du prétraitement, la comparaison des modèles, "
        "l'interprétation des résultats et leur pertinence "
        "dans un contexte d'utilisation réel."
    )
