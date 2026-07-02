import streamlit as st
def show_kpis(df):
    st.header("Business KPI Dashboard")
    total_revenue = df["Revenue"].sum()
    total_orders = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    total_products_sold = df["Quantity"].sum()
    average_order_value = total_revenue / total_orders
    unique_products = df["StockCode"].nunique()
    countries = df["Country"].nunique()
    average_unit_price = df["UnitPrice"].mean()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(
        "Total Revenue",
        f"£{total_revenue:,.2f}"
    )
    col2.metric(
        "Orders",
        f"{total_orders:,}"
    )
    col3.metric(
        "Customers",
        f"{total_customers:,}"
    )
    col4.metric(
        "Products Sold",
        f"{total_products_sold:,}"
    )
    col5, col6, col7, col8 = st.columns(4)
    col5.metric(
        "Avg Order Value",
        f"£{average_order_value:,.2f}"
    )
    col6.metric(
        "Unique Products",
        f"{unique_products:,}"
    )
    col7.metric(
        "Countries",
        f"{countries}"
    )
    col8.metric(
        "Avg Unit Price",
        f"£{average_unit_price:.2f}"
    )