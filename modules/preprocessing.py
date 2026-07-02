import pandas as pd
import streamlit as st
def preprocess_data(df):
    """
    Cleans the uploaded dataset and returns
    a processed DataFrame.
    """
    st.header("🧹 Data Preprocessing")
    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.write("Column Names")
    st.write(df.columns.tolist())
    st.subheader("Missing Values")
    missing = df.isnull().sum()
    st.dataframe(missing)
    numeric_columns = df.select_dtypes(include="number").columns
    df[numeric_columns] = df[numeric_columns].fillna(
        df[numeric_columns].mean()
    )
    categorical_columns = df.select_dtypes(include="object").columns
    df[categorical_columns] = df[categorical_columns].fillna("Unknown")
    st.success("Missing values handled successfully.")
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    st.subheader("Duplicate Removal")
    st.write("Duplicates Removed:", before - after)
    if "PurchaseDate" in df.columns:
        df["PurchaseDate"] = pd.to_datetime(
            df["PurchaseDate"]
        )
        st.success("PurchaseDate converted to DateTime.")
    return df