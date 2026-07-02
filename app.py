import streamlit as st
from modules.upload import upload_dataset
from modules.preprocessing import preprocess_data
from modules.analytics import show_kpis
st.set_page_config(
    page_title="Customer Behavior Analytics",
    layout="wide"
)
st.title("Customer Behavior Analytics Dashboard")
st.write("Welcome to the Customer Behavior Analytics Dashboard!")
st.divider()
df = upload_dataset()
if df is not None:
    cleaned_df = preprocess_data(df)
    show_kpis(cleaned_df)
    st.divider()
    st.subheader("Cleaned Dataset")
    st.dataframe(cleaned_df)
else:
    st.warning("Please upload a dataset.")