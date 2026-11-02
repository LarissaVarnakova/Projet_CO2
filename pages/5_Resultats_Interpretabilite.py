import streamlit as st
import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Résultats et interprétabilité — Projet CO₂",
    page_icon="📊",
    layout="wide"
)

RACINE_PROJET = Path(__file__).resolve().parent.parent
DOSSIER_FIGURES = RACINE_PROJET / "reports" / "figures"


def afficher_figure(nom_fichier, legende, largeur=720):
    chemin = DOSSIER_FIGURES / nom_fichier

    if chemin.exists():
        st.image(str(chemin), width=largeur)
        st.caption(legende)
    else:
        st.warning(f"Figure introuvable : {nom_fichier}")


# ============================================================
# DONNÉES ISSUES DU RAPPORT
# ============================================================

resultats = pd.DataFrame({
    "Modèle": [
        "XGBoost",
        "Random Forest",
        "Arbre de décision",
        "LightGBM",
        "MLP standardisé",
        "Lasso optimisé",
        "Ridge optimisé",
        "Régression linéaire",
        "DummyRegressor"
    ],
    "MAE": [
        0.2908, 0.0925, 0.1423, 0.3701, 0.5863,
        1.0922, 1.0925, 1.0922, 22.4525
    ],
    "RMSE": [
        0.5940, 0.7112, 0.8176, 1.2902, 1.5947,
        1.7401, 1.7401, 1.7402, 34.1556
    ],
    "R²": [
        0.9997, 0.9996, 0.9994, 0.9986, 0.9978,
        0.9974, 0.9974, 0.9974, 0.0
    ],
    "MAPE": [
        0.0017, 0.0006, 0.0010, 0.0021, 0.0034,
        0.0059, 0.0060, 0.0059, 0.1298
    ]
})


# ============================================================
# EN-TÊTE
# ============================================================

st.title("📊 Résultats et interprétabilité")

st.write(
    "Après l'entraînement et l'optimisation des modèles, "
    "nous avons comparé leurs performances sur le jeu de test "
    "et analysé les prédictions du modèle retenu."
)

st.info(
    "Notre objectif : sélectionner un modèle performant "
    "tout en comprenant les variables qui influencent ses prédictions."
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("RMSE XGBoost", "0,5940 g/km")

with col2:
    st.metric("R² XGBoost", "0,9997")

with col3:
    st.metric("MAE Random Forest", "0,0925 g/km")

st.divider()


# ============================================================
# ONGLETS
# ============================================================

onglet1, onglet2, onglet3, onglet4 = st.tabs([
    "📊 Comparaison",
    "🏆 Modèle retenu",
    "🔎 Interprétabilité SHAP",
    "💡 Enseignements"
])


# ============================================================
# ONGLET 1 — COMPARAISON
# ============================================================

with onglet1:

    st.header("Comparaison globale des modèles")

    st.write(
        "Tous les modèles supervisés dépassent largement "
        "le DummyRegressor. Le choix du meilleur modèle "
        "dépend toutefois de la métrique privilégiée."
    )

    tableau = resultats.copy()

    for colonne in ["MAE", "RMSE", "R²", "MAPE"]:
        tableau[colonne] = tableau[colonne].map(
            lambda valeur: f"{valeur:.4f}".replace(".", ",")
        )

    tableau = tableau.rename(columns={
        "MAE": "MAE (g/km)",
        "RMSE": "RMSE (g/km)"
    })

    st.dataframe(
        tableau,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Source : tableau comparaison_modeles du notebook "
        "principal de modélisation."
    )

    st.divider()

    st.subheader("Comparaison graphique")

    metrique = st.radio(
        "Choisir une métrique",
        ["RMSE", "MAE"],
        horizontal=True
    )

    inclure_dummy = st.checkbox(
        "Inclure le DummyRegressor",
        value=False
    )

    donnees_graphique = resultats.copy()

    if not inclure_dummy:
        donnees_graphique = donnees_graphique[
            donnees_graphique["Modèle"] != "DummyRegressor"
        ]

    donnees_graphique = donnees_graphique.sort_values(metrique)

    st.bar_chart(
    donnees_graphique.set_index("Modèle")[[metrique]],
    horizontal=True,
    use_container_width=True
    )

    if metrique == "RMSE":
        st.success(
            "XGBoost présente le RMSE le plus faible : "
            "0,5940 g/km. Cette métrique pénalise davantage "
            "les erreurs importantes."
        )
    else:
        st.success(
            "Random Forest présente la MAE la plus faible : "
            "0,0925 g/km. Il minimise l'erreur absolue moyenne."
        )


# ============================================================
# ONGLET 2 — MODÈLE RETENU
# ============================================================

with onglet2:

    st.header("Pourquoi avons-nous retenu XGBoost ?")

    st.write(
        "XGBoost obtient le meilleur RMSE et le meilleur R² "
        "dans notre comparaison. Nous l'avons retenu "
        "en privilégiant la réduction des erreurs importantes."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("MAE", "0,2908 g/km")
        st.metric("RMSE", "0,5940 g/km")

    with col2:
        st.metric("R²", "0,9997")
        st.metric("MAPE", "0,0017")

    st.warning(
        "Random Forest obtient une meilleure MAE. "
        "Notre sélection repose donc sur le RMSE, "
        "et non sur une supériorité de XGBoost "
        "pour toutes les métriques."
    )

    st.divider()

    st.subheader("Émissions réelles et prédites")

    afficher_figure(
        "xgboost_reel_predit.png",
        "Comparaison des émissions réelles et prédites par XGBoost.",
        largeur=720
    )

    st.write(
        "Ce graphique permet d'observer l'alignement "
        "des prédictions avec les émissions réelles."
    )

    st.divider()

    st.subheader("Analyse des résidus")

    afficher_figure(
        "xgboost_residus.png",
        "Distribution des erreurs de prédiction de XGBoost.",
        largeur=720
    )

    st.write(
        "L'analyse des résidus complète les métriques globales "
        "en permettant d'examiner la dispersion des erreurs."
    )


# ============================================================
# ONGLET 3 — INTERPRÉTABILITÉ SHAP
# ============================================================

with onglet3:

    st.header("Comprendre les prédictions avec SHAP")

    st.write(
        "SHAP (SHapley Additive exPlanations) permet "
        "d'estimer la contribution des variables "
        "aux prédictions du modèle XGBoost."
    )

    st.subheader("1. Graphique SHAP de synthèse")

    afficher_figure(
        "xgboost_shap_synthese.png",
        "Figure 14 — Graphique SHAP de synthèse du modèle XGBoost.",
        largeur=780
    )

    st.write(
        "La consommation mixte est de loin la variable "
        "la plus influente. Les consommations élevées "
        "contribuent à augmenter les émissions prédites, "
        "tandis que les faibles consommations "
        "contribuent à les diminuer."
    )

    st.info(
        "D'autres variables, notamment nox, masse_ordma_max, "
        "puiss_max et certaines modalités du carburant, "
        "interviennent également, mais avec une influence "
        "nettement plus faible."
    )

    st.divider()

    st.subheader("2. Importance globale des variables")

    afficher_figure(
        "xgboost_shap_importance.png",
        "Figure 15 — Importance globale des variables selon SHAP.",
        largeur=780
    )

    st.write(
        "L'importance globale confirme la prédominance "
        "de conso_mixte. Les variables nox, cod_cbr_GO, "
        "masse_ordma_max et puiss_max constituent "
        "un second groupe explicatif."
    )

    st.success(
        "Ces résultats sont cohérents avec notre EDA : "
        "la consommation mixte présentait déjà "
        "une relation très forte avec les émissions de CO₂."
    )

    st.caption(
        "Les contributions SHAP décrivent le fonctionnement "
        "du modèle et ne constituent pas une preuve de causalité."
    )


# ============================================================
# ONGLET 4 — ENSEIGNEMENTS
# ============================================================

with onglet4:

    st.header("Les principaux enseignements")

    st.markdown(
        """
        **1. Les modèles non linéaires sont particulièrement performants.**

        Les modèles linéaires expliquent déjà environ 99,74 %
        de la variance, mais les arbres et les méthodes
        d'ensemble réduisent davantage les erreurs.

        **2. Le choix du modèle dépend de la métrique.**

        Random Forest minimise la MAE et la MAPE,
        tandis que XGBoost minimise le RMSE
        et présente le meilleur R².

        **3. La préparation des données est déterminante.**

        La standardisation améliore fortement le MLP
        dans notre expérimentation contrôlée.

        **4. La consommation mixte joue un rôle central.**

        L'analyse SHAP et les expériences sans
        `conso_mixte` montrent la forte dépendance
        des prédictions à cette variable.
        """
    )

    st.divider()

    st.subheader("Une limite importante")

    st.warning(
        "Les performances très élevées doivent être "
        "interprétées en tenant compte des variables "
        "disponibles au moment de la prédiction. "
        "En particulier, la consommation mixte "
        "est très fortement liée aux émissions de CO₂."
    )

    st.success(
        "Conclusion : XGBoost est retenu pour notre "
        "simulateur, avec un RMSE de 0,5940 g/km "
        "et un R² de 0,9997 sur le jeu de test."
    )
