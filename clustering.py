import streamlit as st
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px  # Pour le tableau et les graphiques interactifs
from sklearn.preprocessing import StandardScaler

def apply_clustering(data):
    st.subheader("Clustering with K-Means")
    
    # Gestion des valeurs manquantes - Imputation ou suppression
    if data.isnull().sum().sum() > 0:
        st.warning("Le jeu de données contient des valeurs manquantes. Nous allons les imputer.")
        data = data.fillna(data.mean())  # Imputation par la moyenne des colonnes

    # Échelle des données avant le clustering
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.select_dtypes(include=['float64', 'int64']))

    # Demander à l'utilisateur de choisir le nombre de clusters
    num_clusters = st.slider("Select number of clusters", 2, 10, 3)
    
    # Appliquer le K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    data["Cluster"] = kmeans.fit_predict(scaled_data)  # On applique sur les données standardisées

    st.write("Clustered Data", data.head())

    # Visualiser les clusters avec PCA
    st.subheader("Cluster Visualization")
    
    # Réduction de la dimensionnalité avec PCA pour la visualisation
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(scaled_data)  # On applique PCA sur les données standardisées
    reduced_data_df = pd.DataFrame(reduced_data, columns=["PCA1", "PCA2"])
    reduced_data_df["Cluster"] = data["Cluster"]

    # Créer un graphique 2D des clusters
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(
        reduced_data_df["PCA1"],
        reduced_data_df["PCA2"],
        c=reduced_data_df["Cluster"],
        cmap="viridis",  # Palette de couleurs
        s=50,
        alpha=0.7
    )
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    plt.colorbar(scatter)
    st.pyplot(fig)  # Afficher le graphique PCA

    # Afficher un tableau interactif avec Plotly
    st.subheader("Interactive Data Table")
    fig_table = px.scatter(
        reduced_data_df, x="PCA1", y="PCA2", color="Cluster", 
        title="PCA Clustering", labels={"PCA1": "Principal Component 1", "PCA2": "Principal Component 2"}
    )
    st.plotly_chart(fig_table)

    # Afficher un tableau des résultats
    st.subheader("Clustering Results Table")
    st.write(data)

    # Statistiques descriptives par cluster
    st.subheader("Cluster Statistics")
    cluster_stats = data.groupby("Cluster").agg(["mean", "std", "min", "max"])
    st.write(cluster_stats)

    # Télécharger les résultats en CSV
    st.subheader("Download Clustered Data")
    csv = data.to_csv(index=False).encode()
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="clustered_data.csv",
        mime="text/csv"
    )
