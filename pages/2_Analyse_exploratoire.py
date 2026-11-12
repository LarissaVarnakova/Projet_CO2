import streamlit as st
from pathlib import Path
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# ============================================================
# CHARGEMENT DES DONNÉES
# ============================================================

RACINE_PROJET = Path(__file__).resolve().parent.parent
CHEMIN_DONNEES = RACINE_PROJET / "data" / "co2_2014.csv"

df_2014 = pd.read_csv(
    CHEMIN_DONNEES,
    encoding="cp1252",
    sep=None,
    engine="python"
)

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
# STYLES ET COMPOSANTS — PAGE EDA
# ============================================================

EDA_STYLES = """
<style>

/* Sous-titre de la page */
.page-subtitle {
    color: #8A94A6;
    font-size: 1.25rem;
    margin-top: -12px;
    margin-bottom: 20px;
}

/* Encadré de présentation de l'objectif */
.objectif-box {
    background-color: #F0F4F8;
    border-left: 5px solid #3B82F6;
    border-radius: 8px;
    padding: 26px 30px;
    margin: 15px 0;
}

/* Libellé de l'objectif */
.objectif-label {
    color: #3B82F6;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

/* Titre de l'objectif */
.objectif-title {
    color: #1E293B;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.4;
    margin-bottom: 20px;
}

/* Description et liste des objectifs */
.objectif-description {
    color: #475569;
    font-size: 1.2rem;
    line-height: 1.5;
}

.objectif-description ul {
    padding-left: 26px;
    margin-bottom: 0;
}

.objectif-description li {
    margin-bottom: 2px;
}

/* Titre des expanders */
div[data-testid="stExpander"] summary p {
    font-size: 20px !important;
    font-weight: 600 !important;
}

/* Taille du texte des boutons radio */
.stRadio div[role="radiogroup"] label p {
    font-size: 1.3rem !important;
}


</style>
"""


st.markdown(EDA_STYLES, unsafe_allow_html=True)

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
df_2014 = pd.read_csv(
    CHEMIN_DONNEES,
    encoding="cp1252",
    sep=None,
    engine="python"
)

# Conversion des colonnes numériques au bon format
colonnes_numeriques = [
    'puiss_max',
    'conso_urb',
    'conso_exurb',
    'conso_mixte',
    'hc',
    'nox',
    'hcnox',
    'ptcl',
    'co_typ_1'
]

for col in colonnes_numeriques:

    df_2014[col] = (
        df_2014[col]
        .astype(str)
        .str.replace(',', '.', regex=False)
    )

    df_2014[col] = pd.to_numeric(
        df_2014[col],
        errors='coerce'
    )


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

    st.subheader("Qualité du jeu de données")

    # ============================================================
    # INDICATEURS CLÉS — STRUCTURE INITIALE DES DONNÉES
    # ============================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="OBSERVATIONS INITIALES",
            value="55 044",
            border=True,
            help="Nombre de lignes du jeu de données initial."
        )

    with col2:
        st.metric(
            label="VARIABLES INITIALES",
            value="30",
            border=True,
            help="Nombre de colonnes du jeu de données initial."
        )

    with col3:
        st.metric(
            label="COLONNES ENTIÈREMENT VIDES",
            value="4",
            border=True,
            help="Variables ne contenant aucune valeur renseignée."
        )
    st.subheader("Principales valeurs manquantes")

        
    # ============================================================
    # ANALYSE DES VALEURS MANQUANTES
    # ============================================================
 
    # Calcul du taux de valeurs manquantes par variable
    taux_null = (
        df_2014.isnull()
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    # Répartition en trois catégories
    null_100 = taux_null[taux_null == 100]

    null_50_100 = taux_null[
        (taux_null >= 50) & (taux_null < 100)
    ]

    null_0_50 = taux_null[
        (taux_null > 0) & (taux_null < 50)
    ]

    # ============================================================
    # AFFICHAGE DES RÉSULTATS EN TROIS COLONNES, DES CATÉGORIES AVEC LISTES DÉPLIABLES
    # ============================================================

    categories = [
        ("100 % — ENTIÈREMENT VIDES", null_100),
        ("50 % À MOINS DE 100 %", null_50_100),
        ("PLUS DE 0 % À MOINS DE 50 %", null_0_50)
    ]

    cols = st.columns(3)

    for col, (titre, variables) in zip(cols, categories):

        with col:
            with st.container(border=True):

                with st.expander(
                    f"{titre} ({len(variables)} variables)",
                    expanded=False
                ):

                    if not variables.empty:
                        for variable, taux in variables.items():
                            st.markdown(
                                f"- **{variable}** : {taux:.2f} %"
                            )
                    else:
                        st.caption("Aucune variable dans cette catégorie.")


    # ============================================================
    # VARIABLES NUMÉRIQUES MAL TYPÉES
    # ============================================================
    st.subheader("Variables numériques mal typées")

    colonnes_numeriques_mal_typees = [
        'puiss_max',
        'conso_urb',
        'conso_exurb',
        'conso_mixte',
        'hc',
        'nox',
        'hcnox',
        'ptcl',
        'co_typ_1'
    ]

    with st.expander(
        f"🔢  ({len(colonnes_numeriques_mal_typees)} variables)",
        expanded=False
    ):

        st.write(
            "Ces variables représentent des données numériques, "
            "mais sont importées avec un type non numérique dans le fichier source "
        )

        for variable in colonnes_numeriques_mal_typees:
            st.markdown(f"- **{variable}**")

# ============================================================
# ONGLET 2 — ANALYSE DESCRIPTIVE
# ============================================================


with onglet2:

    st.header("Analyse des émissions de CO₂")

    # Menu de sélection de l'analyse
    choix_analyse = st.selectbox(
        "Sélectionnez une analyse :",
        [
            "1. Distribution des émissions de CO₂",
            "2. Consommation mixte et émissions de CO₂",
            "3. Émissions selon le type de carburant"
        ],
        index=None,
        placeholder="Choisissez une analyse..."
    )

    
    if choix_analyse == "1. Distribution des émissions de CO₂":


        fig, ax = plt.subplots(figsize=(12, 6))

        sns.histplot(
            df_2014['co2'],
            bins=40,
            kde=True,
            ax=ax
        )

        ax.set_title("Distribution des émissions de CO₂")
        ax.set_xlabel("CO₂ (g/km)")
        ax.set_ylabel("Nombre de véhicules")

        # Affichage dans Streamlit
        st.pyplot(fig, use_container_width=True)

        plt.close(fig)

        st.write(
            "Les émissions présentent une dispersion importante, "
            "ce qui traduit la diversité des véhicules étudiés."
        )

    elif choix_analyse == "2. Consommation mixte et émissions de CO₂":

        from matplotlib.ticker import MultipleLocator

        fig = plt.figure(figsize=(10, 6))

        sns.scatterplot(
            x='conso_mixte',
            y='co2',
            data=df_2014
        )

        plt.title("CO₂ en fonction de la consommation mixte")
        plt.xlabel("Consommation mixte (l/100km)")
        plt.ylabel("CO₂ (g/km)")

        # Graduation tous les 5 l/100 km
        plt.gca().xaxis.set_major_locator(MultipleLocator(5))

        st.pyplot(fig, use_container_width=True)

        plt.close(fig)


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

    elif choix_analyse == "3. Émissions selon le type de carburant":

   
        carburants = {
            'ES': 'Essence',
            'GO': 'Diesel',
            'EE': 'Électrique',
            'EH': 'Hybride essence',
            'GH': 'Hybride diesel',
            'ES/GN': 'Essence / Gaz naturel',
            'GN/ES': 'Gaz naturel / Essence',
            'FE': 'Superéthanol E85',
            'GN': 'Gaz naturel',
            'GL': 'GPL',
            'GP/ES': 'GPL / Essence',
            'ES/GP': 'Essence / GPL'
        }

        df_2014['carburant_libelle'] = df_2014['cod_cbr'].map(carburants)

        fig = plt.figure(figsize=(14, 6))

        sns.boxplot(
            x='carburant_libelle',
            y='co2',
            data=df_2014
        )

        plt.xticks(rotation=30, ha='right')

        plt.title("CO₂ selon le type de carburant")
        plt.xlabel("Type de carburant")
        plt.ylabel("CO₂ (g/km)")

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)

        plt.close(fig)


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

    st.subheader("1. Corrélations entre les variables numériques")

    with st.expander("Matrice de correlation", expanded=False):

        # ============================================================
        # MATRICE DE CORRÉLATION
        # ============================================================

  
        # Variables à exclure : 100 % et 50 % à moins de 100 % de valeurs nulles
        variables_a_exclure = null_100.index.union(null_50_100.index)

        # Sélection des variables numériques
        df_numeric = df_2014.select_dtypes(include="number")

        # Exclusion des variables ayant au moins 50 % de valeurs nulles
        df_numeric = df_numeric.drop(
            columns=variables_a_exclure,
            errors="ignore"
        )

        # Calcul de la matrice de corrélation
        corr_matrix = df_numeric.corr()

        # ============================================================
        # MATRICE DE CORRÉLATION ADAPTATIVE
        # ============================================================

        n = len(corr_matrix)

        # Taille de la figure adaptée au nombre de variables
        fig_width = min(11, max(6, n * 0.30))
        fig_height = min(8, max(5, n * 0.27))

        fig, ax = plt.subplots(
            figsize=(fig_width, fig_height),
            dpi=100
        )

        # Taille des annotations adaptative
        taille_annotations = max(3, min(7, 100 / n))

        sns.heatmap(
            corr_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            center=0,
            vmin=-1,
            vmax=1,
            annot_kws={"size": taille_annotations},
            square=True,
            linewidths=0.2,
            linecolor="white",
            ax=ax
        )

        ax.set_title(
            "Matrice de corrélation des variables numériques",
            fontsize=10,
            pad=10
        )

        ax.tick_params(axis="x", labelsize=6, rotation=45)
        ax.tick_params(axis="y", labelsize=6, rotation=0)

        fig.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.divider()


    st.subheader("2. Tests statistiques")
    # ============================================================
    # TESTS ANOVA
    # ============================================================

    with st.expander("Tests ANOVA", expanded=False):

        # ------------------------------------------------
        # SÉLECTION DU TEST ANOVA
        # ------------------------------------------------

        choix_anova = st.radio(
            "Sélectionner une analyse :",
            [
                "Émissions de CO₂ par carburant",
                "Émissions de CO₂ par gamme commerciale"
            ],
            horizontal=True,
            key="choix_anova"
        )

        # ============================================================
        # TEST 1 — ANOVA : TYPE DE CARBURANT
        # ============================================================

        if choix_anova == "Émissions de CO₂ par carburant":
            st.caption("Analyse des catégories comportant plus de 30 observations.")
            st.write(
            "L'ANOVA met en évidence des différences statistiquement "
            "significatives entre les émissions moyennes de CO₂ "
            "selon le type de carburant. ")
            st.write("Les metriques obtenues montrent qu'ils existe des differences significatives " \
                    "entre au moins deux categories de carburant.")
            carburants = {
                'ES': 'Essence',
                'GO': 'Diesel',
                'EE': 'Électrique',
                'EH': 'Hybr. essence',
                'GH': 'Hybr. diesel',
                'ES/GN': 'Essence/Gaz nat.',
                'GN/ES': 'Gaz nat./Essence',
                'FE': 'Superéthanol E85',
                'GN': 'Gaz nat.',
                'GL': 'GPL',
                'GP/ES': 'GPL/Essence',
                'ES/GP': 'Essence/GPL'
            }

            # ------------------------------------------------------------
            # Préparation des groupes
            # ------------------------------------------------------------

            groupes = {
                carburant: groupe['co2'].dropna().values
                for carburant, groupe in df_2014.groupby('cod_cbr')
                if groupe['co2'].dropna().count() > 30
            }

            # Test ANOVA
            stat, p = stats.f_oneway(*groupes.values())

 
            # ------------------------------------------------------------
            # Résultats du test ANOVA
            # ------------------------------------------------------------

            st.markdown("Résultats du test ANOVA")

            with st.container(width=800):
                col1, col2 = st.columns(2, gap="medium")
 
                with col1:
                    with st.container(border=True):
                        st.markdown("**Statistique F**")
                        st.markdown(f"### {stat:.2f}")

                with col2:
                    with st.container(border=True):
                        st.markdown("**p-value**")
                        st.markdown(f"### {p:.2e}")
            # ------------------------------------------------------------
            # Préparation des données pour le graphique
            # ------------------------------------------------------------

            df_cbr = df_2014[
                df_2014['cod_cbr'].isin(groupes.keys())
            ].copy()

            df_cbr['carburant_libelle'] = (
                df_cbr['cod_cbr'].map(carburants)
                .fillna(df_cbr['cod_cbr'])
            )

            ordre = [
                carburants[c]
                for c in carburants
                if c in groupes
            ]

            # ------------------------------------------------------------
            # Visualisation : boxplot
            # ------------------------------------------------------------

            st.markdown(
                "#### Distribution des émissions de CO₂ par type de carburant"
            )

            fig, ax = plt.subplots(figsize=(9, 4))

            sns.boxplot(
                x='carburant_libelle',
                y='co2',
                data=df_cbr,
                order=ordre,
                palette='Blues',
                ax=ax
            )

            ax.set_xlabel('Type de carburant')
            ax.set_ylabel('CO₂ (g/km)')

            plt.xticks(rotation=20, ha='right')
            plt.tight_layout()

            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # ============================================================
        # TEST 2 — ANOVA : GAMME COMMERCIALE
        # ============================================================

        elif choix_anova == "Émissions de CO₂ par gamme commerciale":

            # ------------------------------------------------------------
            # Préparation des groupes
            # ------------------------------------------------------------

            groupes = {
                nom_gamme: sous_df['co2'].dropna().values
                for nom_gamme, sous_df in df_2014.groupby('gamme')
                if sous_df['co2'].dropna().count() > 30
            }

            # Test ANOVA
            stat, p = stats.f_oneway(*groupes.values())

            # ------------------------------------------------------------
            # Résultats du test ANOVA
            # ------------------------------------------------------------
            
            st.markdown("#### Résultats du test ANOVA")
            with st.container(width=800):
                col1, col2 = st.columns(2, gap="medium")
                
                with col1:
                    with st.container(border=True):
                        st.markdown("**Statistique F**")
                        st.markdown(f"### {stat:.2f}")
                
                with col2:
                    with st.container(border=True):
                        st.markdown("**p-value**")
                        st.markdown(f"### {p:.2e}")
            # ------------------------------------------------------------
            # Visualisation : boxplot
            # ------------------------------------------------------------

            st.markdown(
                "#### Distribution des émissions de CO₂ par gamme commerciale"
            )

            ordre = (
                df_2014.groupby('gamme')['co2']
                .mean()
                .sort_values()
                .index
            )

            fig, ax = plt.subplots(figsize=(8, 4))

            sns.boxplot(
                x='gamme',
                y='co2',
                data=df_2014,
                order=ordre,
                palette='Oranges',
                ax=ax
            )

            ax.set_xlabel('Gamme commerciale')
            ax.set_ylabel('CO₂ (g/km)')

            plt.xticks(rotation=20, ha='right')
            plt.tight_layout()

            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
    # ============================================================
    # TEST DE WELCH — HYBRIDES VS NON-HYBRIDES
    # ============================================================
    with st.expander("Test de Student", expanded=False):
        st.markdown("#### Comparaison des émissions : hybrides vs non-hybrides")


        # Séparation des groupes
        hybrides = df_2014.loc[
            df_2014["hybride"] == "oui", "co2"
        ].dropna()

        non_hybrides = df_2014.loc[
            df_2014["hybride"] == "non", "co2"
        ].dropna()

        # Test t de Welch
        stat, p = stats.ttest_ind(
            hybrides,
            non_hybrides,
            equal_var=False
        )

        # ------------------------------------------------------------
        # AFFICHAGE DES RÉSULTATS
        # ------------------------------------------------------------

        with st.container(width=800):
            col1, col2, col3 = st.columns(3, gap="medium")

            with col1:
                with st.container(border=True):
                    st.metric(
                        "Moyenne hybrides",
                        f"{hybrides.mean():.1f} g/km"
                    )
                    st.caption(f"Effectif : {len(hybrides):,}")

            with col2:
                with st.container(border=True):
                    st.metric(
                        "Moyenne non-hybrides",
                        f"{non_hybrides.mean():.1f} g/km"
                    )
                    st.caption(f"Effectif : {len(non_hybrides):,}")

            with col3:
                with st.container(border=True):
                    st.metric(
                        "Statistique t",
                        f"{stat:.4f}"
                    )

        # ------------------------------------------------------------
        # VISUALISATION — BOXPLOT
        # ------------------------------------------------------------

        fig, ax = plt.subplots(figsize=(7, 4))

        ordre = ["oui", "non"]

        sns.boxplot(
            x="hybride",
            y="co2",
            data=df_2014,
            order=ordre,
            hue="hybride",
            hue_order=ordre,
            palette=["#378ADD", "#C0DD97"],
            legend=False,
            ax=ax
        )

        ax.set_title("Distribution CO₂ — hybride vs non-hybride")
        ax.set_xlabel("Motorisation")
        ax.set_ylabel("CO₂ (g/km)")
        ax.set_xticklabels(["Hybrides", "Non-hybrides"])

        sns.despine()
        fig.tight_layout()

        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        st.write(
            "Le test de Student met en évidence une différence "
            "statistiquement significative entre véhicules "
            "hybrides et non hybrides. Les véhicules hybrides "
            "présentent globalement des émissions plus faibles."
        )
    st.success(
            "Ces tests mettent en évidence des associations statistiques, " \
            "mais ne démontrent pas de relations de causalité")

# ============================================================
# ONGLET 4 — SYNTHÈSE
# ============================================================

with onglet4:

    st.header("Les principaux enseignements de l'EDA")

    st.write(
        "L'exploration et les analyses statistiques nous ont permis "
        "de mieux comprendre les données et d'identifier les éléments "
        "à prendre en compte avant la modélisation."
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        with st.container(border=True):
            st.markdown("### 01 · Qualité des données")
            st.write(
                "Certaines variables sont entièrement vides ou fortement "
                "incomplètes. Un nettoyage et un traitement des valeurs "
                "manquantes sont nécessaires."
            )

        with st.container(border=True):
            st.markdown("### 03 · Caractéristiques techniques")
            st.write(
                "La masse et certaines caractéristiques des véhicules "
                "sont associées aux niveaux d'émissions."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 02 · Consommation de carburant")
            st.write(
                "La consommation mixte est fortement associée aux émissions "
                "de CO₂ et constitue une variable importante pour la prédiction. "
            )

        with st.container(border=True):
            st.markdown("### 04 · Catégories de véhicules")
            st.write(
                "Les analyses ANOVA mettent en évidence des différences "
                "significatives d'émissions selon le carburant, "
                "la carrosserie, la gamme et l'hybridation."
            )

    st.info(
        "**À retenir :** les résultats de l'EDA ont guidé nos choix "
        "de nettoyage, de préparation des données et de sélection "
        "des variables pour la modélisation."
    )