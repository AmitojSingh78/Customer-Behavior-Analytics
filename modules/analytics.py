import streamlit as st
def show_kpis(df):
    """
    Display important business KPIs.
    """
    st.header("Business KPIs")
    total_customers = df["CustomerID"].nunique()
    total_sales = df["Amount"].sum()
    average_purchase = df["Amount"].mean()
    highest_purchase = df["Amount"].max()
    lowest_purchase = df["Amount"].min()
    total_categories = df["Category"].nunique()
    total_cities = df["City"].nunique()
    total_transactions = len(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Customers", total_customers)
    col2.metric("Total Sales", f"₹{total_sales:,.2f}")
    col3.metric("Avg Purchase", f"₹{average_purchase:,.2f}")
    col4.metric("Transactions", total_transactions)
    col5, col6, col7, col8 = st.columns(4)
    col5.metric("Highest Purchase", f"₹{highest_purchase:,.2f}")
    col6.metric("Lowest Purchase", f"₹{lowest_purchase:,.2f}")
    col7.metric("Categories", total_categories)
    col8.metric("Cities", total_cities)