import streamlit as st
import pandas as pd
from modules.preprocessing import preprocess_data
from modules.analytics import show_kpis
from modules.visualisation import show_visualizations
from modules.rfm import show_rfm
from modules.filters import apply_filters
from modules.reports import generate_report
from database.database import create_database
from database.database import run_query
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
st.set_page_config(
    page_title="Customer Purchase Behavior Analytics",
    layout="wide"
)
load_css()
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Visualizations",
        "Customer Segmentation",
        "SQL Dashboard",
        "Reports",
        "About"
    ]
)
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
create_database(clean_df)
clean_df = apply_filters(clean_df)
st.info(
    f"Showing {len(clean_df):,} records after applying filters."
)
if page=="Dashboard":
    show_kpis(clean_df)
elif page=="Visualizations":
    show_visualizations(clean_df)
elif page=="Customer Segmentation":
    show_rfm(clean_df)
elif page == "SQL Dashboard":
    st.title("🗄 SQL Analytics Dashboard")
    query = st.text_area(
        "Write SQL Query",
        "SELECT * FROM transactions LIMIT 10"
    )
    if st.button("Run Query"):
        result = run_query(query)
        st.dataframe(result, use_container_width=True)
elif page=="Reports":
    st.title("Generate Business Report")
    if st.button("Generate PDF Report"):
        report_path = generate_report(clean_df)
        with open(report_path, "rb") as pdf:
            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf,
                file_name="Customer_Analytics_Report.pdf",
                mime="application/pdf"
        )
        st.success("PDF Report Generated Successfully!")
elif page=="About":
    st.title("About Project")
    st.write("""
Customer Purchase Behavior Analytics Dashboard
Built using
- Python
- Streamlit
- Pandas
- Plotly
- Scikit-Learn
Dataset
Online Retail Dataset
    """)
st.divider()
st.subheader("Cleaned Dataset")
st.dataframe(
    clean_df,
    use_container_width=True
)
csv = clean_df.to_csv(index=False).encode()
st.download_button(
    "Download Clean Dataset",
    csv,
    "CleanDataset.csv",
    "text/csv"
)