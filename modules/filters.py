import streamlit as st
def apply_filters(df):
    st.sidebar.header("🔍 Filters")
    countries = sorted(df["Country"].unique())
    selected_country = st.sidebar.multiselect(
        "Select Country",
        countries,
        default=countries
    )
    min_date = df["InvoiceDate"].min().date()
    max_date = df["InvoiceDate"].max().date()
    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    min_revenue = float(df["Revenue"].min())
    max_revenue = float(df["Revenue"].max())
    revenue_range = st.sidebar.slider(
        "Revenue Range",
        min_value=min_revenue,
        max_value=max_revenue,
        value=(min_revenue, max_revenue)
    )
    filtered_df = df[
        (df["Country"].isin(selected_country))
        &
        (df["InvoiceDate"].dt.date >= start_date)
        &
        (df["InvoiceDate"].dt.date <= end_date)
        &
        (df["Revenue"] >= revenue_range[0])
        &
        (df["Revenue"] <= revenue_range[1])
    ]
    return filtered_df