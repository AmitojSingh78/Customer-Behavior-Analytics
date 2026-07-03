from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
def generate_report(df):
    filename = "outputs/Customer_Analytics_Report.pdf"
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []
    title = Paragraph(
        "Customer Purchase Behavior Analytics Report",
        styles["Title"]
    )
    elements.append(title)
    elements.append(Spacer(1,20))
    total_revenue = df["Revenue"].sum()
    total_orders = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    products = df["StockCode"].nunique()
    summary = f"""
<b>Executive Summary</b><br/><br/>
Total Revenue : £{total_revenue:,.2f}<br/>
Total Orders : {total_orders}<br/>
Customers : {total_customers}<br/>
Products : {products}<br/>
Countries Served : {df['Country'].nunique()}
"""
    elements.append(
        Paragraph(summary, styles["BodyText"])
    )
    elements.append(Spacer(1,20))
    top_country = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    country_text = "<b>Top 5 Countries</b><br/><br/>"
    for country, revenue in top_country.items():
        country_text += f"{country} : £{revenue:,.2f}<br/>"
    elements.append(
        Paragraph(country_text, styles["BodyText"])
    )
    elements.append(Spacer(1,20))
    top_products = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    product_text = "<b>Top 5 Products</b><br/><br/>"
    for product, revenue in top_products.items():
        product_text += f"{product} : £{revenue:,.2f}<br/>"
    elements.append(
        Paragraph(product_text, styles["BodyText"])
    )
    elements.append(Spacer(1,20))
    recommendation = """
<b>Business Recommendation</b><br/><br/>
• Focus marketing efforts on high-value customers.<br/>
• Increase inventory for best-selling products.<br/>
• Expand into top-performing countries.<br/>
• Re-engage inactive customers through promotional campaigns.
"""
    elements.append(
        Paragraph(recommendation, styles["BodyText"])
    )
    doc.build(elements)
    return filename