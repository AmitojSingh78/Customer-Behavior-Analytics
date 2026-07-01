import pandas as pd
import streamlit as st
def upload_dataset():
    """
    Upload a CSV or Excel dataset and return it as a Pandas DataFrame.
    """
    uploaded_file = st.file_uploader(
        "Upload Customer Dataset",
        type=["csv", "xlsx"]
    )
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("Dataset uploaded successfully!")
        st.subheader("Dataset Preview")
        st.dataframe(df)
        return df
    return None