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
    fig1 = px.line(
        monthly_sales,
        x="Month",
        y="Revenue",
        title="Monthly Revenue Trend",
        markers=True
    )
    country_sales = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig2 = px.bar(
        country_sales,
        x="Country",
        y="Revenue",
        title="Top 10 Countries by Revenue",
        color="Revenue"
    )
    product_sales = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig3 = px.bar(
        product_sales,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 10 Products by Revenue",
        color="Revenue"
    )
    customer_sales = (
        df.groupby("CustomerID")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig4 = px.bar(
        customer_sales,
        x="CustomerID",
        y="Revenue",
        title="Top 10 Customers by Revenue",
        color="Revenue"
    )
    left, right = st.columns(2)
    with left:
        st.plotly_chart(fig1, use_container_width=True)
    with right:
        st.plotly_chart(fig2, use_container_width=True)
    left, right = st.columns(2)
    with left:
        st.plotly_chart(fig3, use_container_width=True)
    with right:
        st.plotly_chart(fig4, use_container_width=True)