import streamlit as st
from sklearn.ensemble import IsolationForest
import pandas as pd
import matplotlib.pyplot as plt

def detect_anomalies(data):
    st.subheader("Anomaly Detection Using Isolation Forest")

    # Prétraitement des données
    data_clean = data.dropna(axis=0, subset=['Amount', 'Time'])  # Suppression des valeurs manquantes critiques

    # Application de l'Isolation Forest
    model = IsolationForest(contamination=0.05, random_state=42)
    data_clean['Anomaly'] = model.fit_predict(data_clean[['Amount']])

    # Visualisation des anomalies
    st.subheader("Anomaly Detection Visualization")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data_clean['Time'], data_clean['Amount'], c=data_clean['Anomaly'], cmap='coolwarm', s=50, alpha=0.7)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amount')
    st.pyplot(fig)

    # Afficher les anomalies
    st.subheader("Detected Anomalies")
    anomalies = data_clean[data_clean['Anomaly'] == -1]
    st.write(anomalies)

    # Télécharger les anomalies détectées
    st.subheader("Download Anomaly Data")
    csv = anomalies.to_csv(index=False).encode()
    st.download_button(
        label="Download Anomalies CSV",
        data=csv,
        file_name="anomalies_data.csv",
        mime="text/csv"
    )
