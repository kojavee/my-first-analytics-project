import streamlit as st
import pandas as pd

st.title("CSV File Uploader")

df = pd.read_csv("datasets/trips_data_1000.csv")
st.write("### Preview of Uploaded Data:")
st.dataframe(df.head())


