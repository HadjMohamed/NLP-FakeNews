import streamlit as st
from streamlit_timeline import timeline
import json
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import os 

current_dir = os.path.dirname(__file__)
def path_to_image(image_name):
    image_path = os.path.join(current_dir, "images")
    image_path=os.path.join(current_dir, image_path,image_name)
    return image_path

st.set_page_config(
    page_title="Aperçu du Projet",
    layout="wide"
)

# Selectbox pour choisir la langue
lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])

# Contenu en fonction de la langue sélectionnée
if lang == "English":
    tab1, tab2,tab3,tab4= st.tabs(["The project itself","📂 General structure", "🤖 Our Model", "🚀 Improvement Areas"])
    with tab1:
        st.title("🧭 Project Overview")

        st.markdown("""
        Welcome to the **Reddit Fake News Detector** – a data-driven system designed to classify news headlines from Reddit's r/worldnews as *real* or *fake* using natural language processing and machine learning.
        For this project, we had 2 weeks to build a **proof of concept**. The goal was to create a **pipeline** that could be used to scrape, store, and analyze news headlines from the worldNews Reddit and check their veracity.
        The project is built using **Python** and various libraries such as **Streamlit**, **Pandas**, and **Scikit-learn**. The machine learning model is based on the **BERT** architecture, which is fine-tuned for the task of fake news detection.
        This page presents the **global architecture** and the **components** of our pipeline.
        """)

        # 🖼️ Schéma d'architecture
        st.header("📌 Global Architecture")

        st.image(path_to_image("global_pipeline.png"), caption="Overview of the project architecture")

        # 🔄 Etapes
        st.header("⚙️ System Components")

        st.markdown("""
        Here’s a breakdown of the pipeline:

        1. **🔍 Data Collection**
        - We scrape new posts from [r/worldnews](https://www.reddit.com/r/worldnews/new/) daily.
        - Metadata includes: title, source, author, timestamp, URL.

        2. **📥 Data Storage**
        - All the data is stored in **Google BigQuery**.
        - Tables are updated automatically every 24 hours.

        3. **🧠 Machine Learning Model**
        - A **BERT-based model** is used to classify each title as *fake* or *real*.
        - Predictions are stored back in the database.

        4. **📊 Interactive Dashboard**
        - Built with **Streamlit** to display:
            - Filterable news tables
            - Prediction results
            - Performance metrics (F1, Accuracy, etc.)

        """)


        st.success("💡 You can explore the live dashboard using the sidebar!")
        # 🗺️ Roadmap
        st.header("📅 Roadmap")
        
        with open(os.path.join(current_dir, "timeline.json"), "r") as f:
            data = json.load(f)

        # Affichage de la timeline
        timeline(data, height=700)
    with tab2:
        st.title("Apache Airflow")

        st.header("What is Airflow?")
        st.markdown("""
        Apache Airflow is an open-source workflow orchestration platform that allows you to create, schedule, and monitor workflows.
        """)

        st.header("What is a DAG?")
        st.markdown("""
        A **DAG** (Directed Acyclic Graph):

        - It describes a series of steps to follow
        - In a specific order
        - Without ever going backwards (hence "acyclic")

        In Airflow, these steps are called tasks, and the DAG is the structure that connects them.
        """)

        st.header("To summarize")
        st.markdown("""
        - Automate repetitive processes
        - Get an overview of task execution
        - Track the state of tasks
        """)

        st.write("Here is the overall goal of the project with the two existing DAGs:")
        st.image(path_to_image("airflow_copie.png"), caption="Execution DAG")
        st.write("The model_to_bq DAG")
        st.image(path_to_image("dag_airflow.png"), caption="Model DAG")
        st.image(path_to_image("ariflow.png"), caption="DAG Graph")

        st.write("This entire architecture is then deployed using IaC (Infrastructure as Code) with Terraform. Terraform is an open-source tool that allows you to create, manage, and provision cloud infrastructure using code.")
        st.image(path_to_image("infrastructure_fakenews.png"), caption="IaC")
    with tab3:
        st.write("For training our model, we used the  datasets Fake.csv and True.csv from Kaggle.")
        st.write("""
                **Dataset**: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
                
                - **Fake.csv**: Contains 23502 fake news headlines and their corresponding labels.
                
                - **True.csv**: Contains 21417 real news headlines and their corresponding labels.
                
                Let's have a look at the most frequent words in each dataset.
                """)
        st.image(path_to_image("wordcloudfake.png"))
        st.image(path_to_image("wordcloudtrue.png"))
        st.write("""
                The model was trained using a **BERT-based** architecture, which is a transformer model pre-trained on a large corpus of text data. 
                The model was fine-tuned on the fake news dataset to learn the specific patterns and features that distinguish fake news from real news.
                
                Finally we obtained a model with an accuracy of **97%** on the test set.
                Here is an example of how the model treats a sentence and the result associated.
                """)
        st.image(path_to_image("shap.png"))
        st.image(path_to_image("result.png"))
    with tab4:
        st.markdown("""
    💡 Here are some key areas for future improvements to make the project even more robust and impactful:

    ### 📚 Data & Model
    - **Balance the training dataset** to avoid biased predictions.
    - **Experiment with alternative models** like DistilBERT or multilingual transformers.
    - **Data augmentation**: apply paraphrasing, synonym replacement, or back-translation techniques to enrich the dataset.

    ### 🧑‍💻 User Interface (Streamlit)
    -  **Add more interactive visualizations** such as bar charts, heatmaps, and timelines.
    -  **Allow users to submit custom news URLs** for live predictions and fact-checking.
    -  **Expand coverage to other subreddits** like r/news, r/politics, r/technology

    ### 🔗 Cross-Source Validation
    -  **Leverage citation networks** to validate news by checking how often an article or its claims are referenced by trusted outlets.
    -  **Build a source graph**: link articles by shared citations or referenced URLs.
    -  **Score trustworthiness** not just from language, but from cross-source validation mechanisms.

    """)
    
elif lang== "Français":
    tab1, tab2, tab3, tab4 = st.tabs(["Le projet", "📂 Structure générale", "🤖 Notre modèle", "🚀 Domaines d'amélioration"])
    
    with tab1:
        st.title("🧭 Aperçu du projet")

        st.markdown("""
        Bienvenue dans le **Détecteur de Fake News sur Reddit** – un système basé sur les données conçu pour classer les titres d'actualités de `r/worldnews` de Reddit en *véridique* ou *mensonger* en utilisant le traitement du langage naturel et l'apprentissage automatique.
        Pour ce projet, nous avons eu 2 semaines pour construire une **preuve de concept**. L'objectif était de créer une **pipeline** qui pourrait être utilisée pour scraper, stocker et analyser les titres d'actualités de Reddit et vérifier leur véracité.
        Le projet est construit en utilisant **Python** et diverses bibliothèques comme **Streamlit**, **Pandas** et **Scikit-learn**. Le modèle d'apprentissage automatique est basé sur l'architecture **BERT**, qui est ajustée pour la tâche de détection de fake news.
        Cette page présente l'**architecture globale** et les **composants** de notre pipeline.
        """)

        # 🖼️ Schéma d'architecture
        st.header("📌 Architecture globale")
        st.image(path_to_image("global_pipeline.png"), caption="Overview of the project architecture")

        # 🔄 Etapes
        st.header("⚙️ Composants du système")

        st.markdown("""
        Voici une répartition de la pipeline :

        1. **🔍 Collecte des données**
        - Nous récupérons quotidiennement de nouveaux posts de [r/worldnews](https://www.reddit.com/r/worldnews/new/).
        - Les métadonnées incluent : titre, source, auteur, timestamp, URL.

        2. **📥 Stockage des données**
        - Toutes les données sont stockées dans **Google BigQuery**.
        - Les tables sont mises à jour automatiquement toutes les 24 heures.

        3. **🧠 Modèle d'apprentissage automatique**
        - Un modèle **basé sur BERT** est utilisé pour classer chaque titre en *faux* ou *véridique*.
        - Les prédictions sont stockées dans la base de données.

        4. **📊 Tableau de bord interactif**
        - Construit avec **Streamlit** pour afficher :
            - Des tables d'articles filtrables
            - Les résultats des prédictions
            - Les métriques de performance
        """)
        
        # 🗺️ Roadmap
        st.header("📅 Roadmap")
        
        with open(os.path.join(current_dir, "timeline.json"), "r") as f:
            data = json.load(f)

        # Affichage de la timeline
        timeline(data, height=700)


    with tab2:
        st.title("Apache Airflow")

        st.header("Qu'est-ce qu'Airflow ?")
        st.markdown("""
        Apache Airflow est une plateforme open-source d'orchestration de workflows qui vous permet de créer, planifier et surveiller des workflows.
        """)

        st.header("Qu'est-ce qu'un DAG ?")
        st.markdown("""
        Un **DAG** (Directed Acyclic Graph) :

        - Il décrit une série d'étapes à suivre
        - Dans un ordre spécifique
        - Sans jamais revenir en arrière (d'où "acyclique")

        Dans Airflow, ces étapes sont appelées des tâches, et le DAG est la structure qui les relie.
        """)

        st.header("Pour résumer")
        st.markdown("""
        - Automatiser des processus répétitifs
        - Obtenir une vue d'ensemble de l'exécution des tâches
        - Suivre l'état des tâches
        """)

        st.write("Voici l'objectif global du projet avec les deux DAGs existants :")
        st.image(path_to_image("airflow_copie.png"), caption="DAG d'exécution")
        st.image(path_to_image("dag_airflow.png"), caption="DAG du modèle")
        st.image(path_to_image("ariflow.png"), caption="Graphique du DAG")

        st.write("Toute cette architecture est ensuite déployée avec l'IaC (Infrastructure as Code) avec Terraform. Terraform est un outil open-source qui permet de créer, gérer et provisionner des infrastructures cloud en utilisant du code.")
        st.image(path_to_image("infrastructure_fakenews.png"), caption="IaC")


    with tab3:
        st.write("Pour entraîner notre modèle, nous avons utilisé les ensembles de données Fake.csv et True.csv de Kaggle.")
        st.write("""
                    **Dataset**: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
                 
                    - **Fake.csv** : Contient 23 502 fake news et leurs étiquettes correspondantes.
                    - **True.csv** : Contient 21 417 vraies articles et leurs étiquettes correspondantes.
                 
                    Voyons les mots les plus fréquents dans chaque jeu de données.
                 """)
        st.image(path_to_image("wordcloudfake.png"))
        st.image(path_to_image("wordcloudtrue.png"))
        st.write("""
                    Le modèle a été entraîné avec une architecture **basée sur BERT**, un modèle de transformateur pré-entraîné sur un grand corpus de données textuelles. 
                    Le modèle a été ajusté sur l'ensemble de données des fake news pour apprendre les motifs et les caractéristiques spécifiques qui distinguent les fake news des vraies news.
                    
                    Enfin, nous avons obtenu un modèle avec une précision de **97%** sur l'ensemble de test.
                    Voici un exemple de la manière dont le modèle traite une phrase et le résultat associé.
                 """)
        st.image(path_to_image("shap.png"))
        st.image(path_to_image("result.png"))


    with tab4:
        st.markdown("""
        Comme tout projet, des améliorations sont possibles, en voici que nous avons jugés pertinentes d'évoquer:

        ### 📚 Meilleur modèle et jeu de données 
        - **Équilibrer l'ensemble de données d'entraînement** pour éviter des prédictions biaisées.
        - **Expérimenter avec des modèles alternatifs** comme DistilBERT ou des transformateurs multilingues.
        - **Augmentation des données** : appliquer des techniques de paraphrase, de remplacement de synonymes ou de back-translation pour enrichir l'ensemble de données.

        ### 🧑‍💻 Interface utilisateur (Streamlit)
        - **Ajouter plus de visualisations interactives** telles que des diagrammes en barres, des cartes thermiques et des chronologies.
        - **Permettre aux utilisateurs de soumettre des URLs de nouvelles personnalisées** pour des prédictions en direct et de la vérification des faits.
        - **Étendre la couverture à d'autres subreddits** comme `r/news`, `r/politics`, `r/technology`.

        ### 🔗 Validation croisée des sources
        - **Utiliser des réseaux de citations** pour valider les articles en vérifiant combien de fois un article ou ses affirmations sont référencés par des médias de confiance.
        - **Construire un graphique de sources** : lier les articles par citations partagées ou URLs référencées.
        - **Évaluer la fiabilité** non seulement à partir du langage, mais aussi à partir des mécanismes de validation croisée des sources.
        """)
