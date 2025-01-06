import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from eda import perform_eda
from clustering import apply_clustering
from anomaly_detection import detect_anomalies

# Configurer la page
st.set_page_config(
    page_title="Credit Card Anomaly Detection Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Appliquer le CSS personnalisé
st.markdown("""
    <style>
        /* Change background color for the main container */
        .block-container {
            background-color: #c0c0c0;
            color: black;
        }

        /* Style for the sidebar */
        /* Targeting the sidebar by using the class '.sidebar' */
        .sidebar .sidebar-content {
            background-color: #003366;  /* Blue background */
            color: white;
        }

        /* Change the color of the page title */
        .css-1v3fvcr {
            color: #333;
        }

        /* Optionally, you can also change the font style */
        body {
            font-family: Arial, sans-serif;
        }

        /* Customize the sidebar menu items */
        .css-1pdp22n {
            color: white;
        }

        /* Customize the sidebar header */
        .css-1y2d8yy {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Barre latérale de navigation
st.sidebar.title("🌐 Navigation")
options = {
    "Home": "🏠",  # Emoji for Home
    "EDA": "📊",  # Emoji for EDA (chart)
    "Clustering": "🔍 ",  # Emoji for Clustering (tools)
    "Anomaly Detection": "⚠️",  # Emoji for Anomaly Detection (warning)
}

# Sidebar navigation
choice = st.sidebar.radio(
    "Go to", 
    options.keys(), 
    format_func=lambda x: f"{options[x]} {x}",  # Add emoji to the option text
)

# Tableau de bord principal
if choice == "Home":
    st.title("Tableau de bord de détection d'anomalies sur les cartes de crédit 💳 ")
    st.write(
        """
        Bienvenue sur le tableau de bord de détection d'anomalies pour les transactions de cartes de crédit.  
        Cette application a pour objectif de fournir une solution puissante et intuitive pour détecter les comportements inhabituels ou frauduleux dans les transactions des cartes de crédit. Voici les principales fonctionnalités offertes par l'application :
        
        1. **Analyse exploratoire des données (EDA)** : 
            Vous pouvez explorer en profondeur les jeux de données relatifs aux transactions de cartes de crédit, comprendre leurs structures et identifier des tendances ou des anomalies potentielles. Cela vous aide à mieux comprendre les données avant d'appliquer des modèles d'analyse.
        
        2. **Techniques de clustering** : 
            Nous appliquons des algorithmes de clustering tels que le K-means ou DBSCAN pour regrouper les transactions similaires. Ces méthodes permettent d'identifier des groupes de comportements similaires, ce qui est essentiel pour repérer des anomalies dans les transactions de cartes de crédit.
        
        3. **Détection des anomalies** :
            En utilisant des techniques d'apprentissage automatique, cette application détecte automatiquement les transactions suspectes ou anormales. Les anomalies sont signalées pour être examinées plus en détail, afin de minimiser les risques de fraude.
        
        4. **Détection en temps réel** :
            Notre solution offre également une fonction de détection en temps réel des anomalies dans les transactions de cartes de crédit. Cela permet de prévenir les fraudes ou d'identifier rapidement des comportements inhabituels dès qu'ils se produisent.
        
        En résumé, cette application vise à fournir une analyse complète des transactions de cartes de crédit et à détecter de manière proactive les fraudes potentielles en utilisant des approches statistiques et d'apprentissage automatique avancées.
        """
    )

elif choice == "EDA":
    st.header("Analyse Exploratoire des Données (EDA)")
    st.write("""
        Cette page est dédiée à l'**analyse exploratoire des données (EDA)**. L'EDA permet de comprendre la structure et les caractéristiques d'un jeu de données avant d'appliquer des modèles d'apprentissage automatique.
        
        Vous pouvez télécharger votre fichier de données (au format CSV) pour visualiser les principales statistiques descriptives, les tendances et les anomalies dans les données.  
        L'EDA inclut la vérification des valeurs manquantes, la distribution des variables, ainsi que l'identification des relations possibles entre les différentes colonnes.
        
        Cette étape est cruciale pour mieux comprendre les données et décider des prochaines étapes dans le processus de détection des anomalies.
    """)
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Aperçu des données:", data.head())
        perform_eda(data)

elif choice == "Clustering":
    st.header("Analyse de Clustering")
    st.write("""
        Cette page vous permet d'appliquer des techniques de **clustering** pour identifier des groupes de données similaires dans votre jeu de données.  
        Le clustering est une méthode d'apprentissage non supervisée utilisée pour regrouper des éléments en fonction de leurs caractéristiques similaires.  
        L'objectif ici est de détecter des anomalies en trouvant des comportements ou des motifs qui diffèrent des groupes principaux.  
        Par exemple, dans le cadre des transactions de cartes de crédit, le clustering peut vous aider à repérer des comportements suspects ou inhabituels qui méritent une attention particulière.
    """)
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        apply_clustering(data)

elif choice == "Anomaly Detection":
    st.header("Détection des Anomalies en Temps Réel")
    st.write("""
        Cette page est dédiée à la **détection des anomalies en temps réel** dans les transactions de cartes de crédit. L'objectif est d'identifier les comportements suspects ou anormaux dans les transactions, afin de prévenir les fraudes.
        
        Vous pouvez télécharger un fichier de transactions (au format CSV) et appliquer des algorithmes de détection des anomalies pour repérer les transactions potentiellement frauduleuses.
        
        Grâce à l'algorithme, nous détectons les points de données qui s'écartent significativement du comportement habituel, indiquant ainsi des anomalies. Cette approche permet d'assurer la sécurité et la fiabilité des transactions en temps réel.
    """)
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        detect_anomalies(data)
