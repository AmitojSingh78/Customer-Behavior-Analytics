import pandas as pd
import streamlit as st
def preprocess_data(df):
    st.header("Data Cleaning Report")
    st.subheader("Original Dataset")
    col1, col2 = st.columns(2)
    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum())
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    st.success(f"Removed {duplicates} duplicate rows.")
    cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
    cancelled_orders = cancelled.sum()
    df = df[~cancelled]
    st.success(f"Removed {cancelled_orders} cancelled invoices.")
    before = len(df)
    df = df[df["Quantity"] > 0]
    removed_quantity = before - len(df)
    st.success(f"Removed {removed_quantity} rows with invalid Quantity.")
    before = len(df)
    df = df[df["UnitPrice"] > 0]
    removed_price = before - len(df)
    st.success(f"Removed {removed_price} rows with invalid Unit Price.")
    before = len(df)
    df = df.dropna(subset=["CustomerID"])
    removed_customer = before - len(df)
    st.success(f"Removed {removed_customer} rows with missing CustomerID.")
    df["Description"] = df["Description"].fillna("Unknown Product")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    st.success("Revenue column created successfully.")
    return df