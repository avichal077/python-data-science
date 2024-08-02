import streamlit as st
import pandas as pd
import plotly.express as px


#ui configuration
st.set_page_config(
    page_title = "pokemon app",
    page_icon = "🫏",
    layout="wide",

)
#load data 
@st.cache_data
def load_data():
    return pd.read_csv("pokemon.csv")
#ui integration
with st.spinner("loading dataset..."):
    df = load_data()
    st.balloons()

st.title("pokemon data analytics")
st.subheader("A simple data app to analyze pokemon data")

st.sidebar.title("menu")
choice = st.sidebar.radio("options",["view data","visualize data"])

if choice == 'view data':
    st.header("view dataset")
    st.dataframe(df)
else:
    st.header("visualization")

#to run this program , open terminal and run thr following command
# streamlit run app.py
