import streamlit as st
from modules.upload import upload_dataset
st.set_page_config(
    page_title="Customer Behavior Analytics",
    layout="wide"
)
st.title("Customer Behavior Analytics Dashboard")
st.write("Welcome to the Customer Behavior Analytics Dashboard!")
st.divider()
df = upload_dataset()
if df is not None:
    st.info(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
else:
    st.warning("Please upload a dataset to continue.")