import streamlit as st
import plotly.express as px
def show_visualizations(df):
    st.header("Interactive Visualizations")
    df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    monthly_sales = (
        df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )
    fig = px.line(
        monthly_sales,
        x="Month",
        y="Revenue",
        title="Monthly Revenue Trend",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)
    country_sales = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        country_sales,
        x="Country",
        y="Revenue",
        title="Top 10 Countries by Revenue",
        color="Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)
    product_sales = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        product_sales,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 10 Products by Revenue",
        color="Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)
    customer_sales = (
        df.groupby("CustomerID")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        customer_sales,
        x="CustomerID",
        y="Revenue",
        title="Top 10 Customers by Revenue",
        color="Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)