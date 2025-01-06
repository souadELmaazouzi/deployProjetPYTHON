import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(data):
    st.subheader("Data Overview")
    st.write(data.describe())
    
    st.subheader("Correlation Matrix")
    corr = data.corr()
    
    # Créer une figure avant d'appeler st.pyplot()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    
    # Passer la figure à st.pyplot()
    st.pyplot(fig)
    
    # Fermer la figure après l'affichage
    plt.close(fig)
    
    st.subheader("Distribution of Features")
    for column in data.columns:
        st.write(f"Distribution of {column}")
        fig, ax = plt.subplots()
        sns.histplot(data[column], kde=True, ax=ax)
        st.pyplot(fig)
        
        # Fermer la figure après l'affichage
        plt.close(fig)

    # Ajouter un graphique de séries temporelles (si la colonne 'Time' est présente)
    if 'Time' in data.columns:
        st.subheader("Time Series Plot")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=data, x='Time', y='Amount', ax=ax)
        st.pyplot(fig)
        
        # Fermer la figure après l'affichage
        plt.close(fig)
