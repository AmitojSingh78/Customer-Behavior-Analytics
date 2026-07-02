import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px
def show_rfm(df):
    st.header("👥 Customer Segmentation (RFM Analysis)")
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    rfm = (
        df.groupby("CustomerID")
        .agg({
            "InvoiceDate": lambda x: (reference_date - x.max()).days,
            "InvoiceNo": "nunique",
            "Revenue": "sum"
        })
        .reset_index()
    )
    rfm.columns = [
        "CustomerID",
        "Recency",
        "Frequency",
        "Monetary"
    ]
    st.subheader("RFM Table")
    st.dataframe(rfm.head())
    model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )
    rfm["Cluster"] = model.fit_predict(
        rfm[["Recency", "Frequency", "Monetary"]]
    )
    st.subheader("Cluster Distribution")
    st.write(
        rfm["Cluster"].value_counts()
    )
    fig = px.scatter(
        rfm,
        x="Frequency",
        y="Monetary",
        color=rfm["Cluster"].astype(str),
        hover_data=["CustomerID"],
        title="Customer Segments"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    return rfm