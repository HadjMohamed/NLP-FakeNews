import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

st.set_page_config(
    page_title="Fake News Dashboard",
    layout="wide"
)

# 🌐 Langue
lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])

# 🔐 Authentification GCP
gcp_secrets = st.secrets["gcp_service_account"]
dataset_info = st.secrets["id"]
project_id = gcp_secrets["project_id"]
dataset = dataset_info["dataset"]
table = dataset_info["table1"]

credentials = service_account.Credentials.from_service_account_info(gcp_secrets)
client = bigquery.Client(credentials=credentials, project=project_id)

# 📥 Chargement des données
@st.cache_data(ttl=86400)
def get_data():
    query = f"SELECT title, date_reference, scrapping_status, score, prediction, url FROM `{project_id}.{dataset}.{table}`"
    df = client.query(query).to_dataframe()
    df['date_reference'] = pd.to_datetime(df['date_reference'])
    df['prediction'] = df['prediction'].str.strip()
    df.columns = ['Title', 'Date', 'Status', 'Score', 'Prediction','URL']
    return df

# 🔁 Rafraîchissement manuel
if st.sidebar.button("🔁 Refresh data / Rafraîchir les données"):
    st.cache_data.clear()

df = get_data()

# === 🇬🇧 ENGLISH VERSION ===
if lang == "English":
    st.title("Welcome to the Reddit Fake News Detector!")
    st.markdown("""
    This dashboard provides real-time insights into the classification of [r/worldnews](https://www.reddit.com/r/worldnews/new/) articles.  
    The data is refreshed every 24 hours.
    """)

    st.title("📰 News Live Table")
    st.caption("Real-time data from Google BigQuery – refreshed every 24h.")

    with st.expander("🔎 Filter options"):
        predictions = st.multiselect(
            "Select News Type(s)", 
            options=df['Prediction'].unique(), 
            default=list(df['Prediction'].unique())
        )
        df = df[df['Prediction'].isin(predictions)]

    st.dataframe(
        df,
        column_config={
            "URL": st.column_config.LinkColumn(),
        },
        hide_index=True,
    )

# === 🇫🇷 VERSION FRANÇAISE ===
else:
    st.title("Bienvenue sur le détecteur de Fake News Reddit !")
    st.markdown("""
    Ce tableau de bord fournit une analyse en temps réel des articles postés sur [r/worldnews](https://www.reddit.com/r/worldnews/new/).  
    Les données sont mises à jour toutes les 24 heures.
    """)

    st.title("📰 Actualités en direct")
    st.caption("Données issues de Google BigQuery – actualisées toutes les 24h.")

    with st.expander("🔎 Options de filtrage"):
        predictions = st.multiselect(
            "Sélectionner le(s) type(s) de news", 
            options=df['Prediction'].unique(), 
            default=list(df['Prediction'].unique())
        )
        df = df[df['Prediction'].isin(predictions)]

    st.dataframe(
        df,
        column_config={
            "URL": st.column_config.LinkColumn(),
        },
        hide_index=True,
    )
