import streamlit as st
import pandas as pd
from modules.preprocessing import preprocess_data
from modules.analytics import show_kpis
from modules.visualisation import show_visualizations
st.set_page_config(
    page_title="Customer Purchase Behavior Analytics",
    layout="wide"
)
st.sidebar.title("Navigation")
st.sidebar.write("Customer Purchase Behavior Analytics")
st.title("Customer Purchase Behavior Analytics Dashboard")
st.markdown("""
Analyze customer purchasing behavior using the Online Retail dataset.
""")
st.divider()
try:
    df = pd.read_csv(
        "data/OnlineRetail.csv",
        encoding="ISO-8859-1"
    )
    st.success("Dataset Loaded Successfully!")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()
st.subheader("Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())
st.divider()
st.subheader("Dataset Columns")
st.write(df.columns.tolist())
st.divider()
clean_df = preprocess_data(df)
st.divider()
show_kpis(clean_df)
st.divider()
show_visualizations(clean_df)
st.divider()
st.subheader("Cleaned Dataset")
st.dataframe(
    clean_df,
    use_container_width=True
)