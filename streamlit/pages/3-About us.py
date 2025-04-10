import streamlit as st

st.set_page_config(page_title="About the Project", layout="centered")

# 🌐 Language selector
lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])

# === 🇬🇧 ENGLISH VERSION ===
if lang == "English":
    st.title("📘 About this Fake News Detection Project")

    st.markdown("""
    ### 🤖 Goal

    This project aims to detect and classify news articles based on their trustworthiness.  
    By leveraging data collected from various sources and running them through an ML model,  
    we assign each article one of the following predictions:

    - **Fake news**
    - **Suspicious news**
    - **Trustful news**
    - **Real news**

    ### 🛠 Tech stack

    - **RedditAPI** for scraping news articles from [r/worldnews](https://www.reddit.com/r/worldnews/new/)
    - **Google Cloud Platform (BigQuery)** for storing and querying large-scale news data
    - **Python & FastAPI** for data processing and machine learning
    - **Airflow** for orchestrating data pipelines
    - **Streamlit** for interactive visualization
    - **[GitHub](https://github.com/HadjMohamed/NLP-FakeNews)** for version control and collaboration
    - **Scheduled updates every 24h**

    ### 💡 Why this matters

    With the growing spread of misinformation online, this tool helps users visualize how content from different authors and sources is classified, and allows for quick, live access to structured insights.

    ### 🧑‍💻 Author

    Built with ❤️ by four enthusiasts:
    - Wissem Abdeljaouad
    - Mohamed Hadj 
    - Erwann Leletty
    - Gauthier Magne
    """)

# === 🇫🇷 VERSION FRANÇAISE ===
else:
    st.title("📘 À propos de ce projet de détection de Fake News")

    st.markdown("""
    ### 🤖 Objectif

    Ce projet a pour but de détecter et classifier les articles de presse selon leur degré de fiabilité.  
    En exploitant des données issues de différentes sources et en les passant à travers un modèle ML,  
    chaque article est classé selon les prédictions suivantes :

    - **Fake news**
    - **Article suspect**
    - **Article fiable**
    - **Vraie information**

    ### 🛠 Technologies utilisées

    - **RedditAPI** pour scrapper les articles du subreddit [r/worldnews](https://www.reddit.com/r/worldnews/new/)
    - **Google Cloud Platform (BigQuery)** pour le stockage et les requêtes sur les données
    - **Python & FastAPI** pour le traitement et l’analyse via machine learning
    - **Airflow** pour l’orchestration des pipelines
    - **Streamlit** pour l’interface interactive
    - **[GitHub](https://github.com/HadjMohamed/NLP-FakeNews)** pour le versioning et le travail collaboratif
    - **Mise à jour automatique toutes les 24h**

    ### 💡 Pourquoi ce projet ?

    Avec la prolifération de la désinformation en ligne, cet outil permet de visualiser comment le contenu est classifié par source, et d’avoir un accès rapide et structuré aux informations.

    ### 🧑‍💻 Auteurs

    Construit avec ❤️ par quatre passionnés :
    - Wissem Abdeljaouad
    - Mohamed Hadj 
    - Erwann Leletty
    - Gauthier Magne
    """)
