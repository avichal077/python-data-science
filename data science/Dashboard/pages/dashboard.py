import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns 
# load the titanic dataset 
titanic = sns.load_dataset("titanic")
st.title("titanic dataset dashboard")
st.sidebar.header("filter options")

st.dataframe(titanic)