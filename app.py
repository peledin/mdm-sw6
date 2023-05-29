import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

df = load_data()

# Sidebar options
st.sidebar.title("Filters")

# Country selection
countries = st.sidebar.multiselect("Choose countries", df['Country'].unique())

# Year selection
year_range = st.sidebar.slider("Choose years", int(df['Year'].min()), int(df['Year'].max()), (int(df['Year'].min()), int(df['Year'].max())))

# Filter data
if countries:
    df = df[df['Country'].isin(countries)]

df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Display data
st.write(df)
