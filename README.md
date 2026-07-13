# Customer-Behavior-Analytics
# Customer Purchase Behavior Analytics Dashboard

## Overview

The **Customer Purchase Behavior Analytics Dashboard** is an interactive business intelligence application developed using **Python** and **Streamlit**. It enables users to analyze customer purchasing patterns from the **Online Retail Dataset** through interactive dashboards, visualizations, customer segmentation, SQL analytics, and automated report generation.

The project demonstrates the complete data analytics workflow, including data preprocessing, exploratory analysis, business intelligence dashboards, customer segmentation using the RFM model, and SQL-based querying.

---

## Features

### Dashboard

* Dataset overview
* Key Performance Indicators (KPIs)
* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Cleaned dataset preview
* Download cleaned dataset

### Interactive Visualizations

* Monthly Revenue Trend
* Top Selling Products
* Top Countries by Revenue
* Revenue Distribution
* Customer Purchase Analysis
* Interactive Plotly charts

### Customer Segmentation

* RFM (Recency, Frequency, Monetary) Analysis
* Customer segmentation into different categories
* Customer insights for targeted marketing

### SQL Analytics Dashboard

* Execute custom SQL queries
* View query results instantly
* Analyze transactional data using SQLite

### Report Generation

* Generate business analytics reports
* Download report in PDF format

---

## Technologies Used

### Programming Language

* Python 3.x

### Framework

* Streamlit

### Libraries

* Pandas
* NumPy
* Plotly
* Scikit-learn
* SQLite3
* ReportLab

---

## Project Structure

```
CustomerPurchaseAnalytics/
|-- app.py
│
|--assets/
│   |-- style.css
│
|-- data/
│   |-- OnlineRetail.csv
│
|-- database/
│   |-- database.py
│
|--modules/
│   |-- preprocessing.py
│   |-- analytics.py
│   |-- visualisation.py
│   |-- filters.py
│   |-- rfm.py
│   |-- reports.py
│
|--requirements.txt
│
|-- README.md
```

---

## Dataset

This project uses the **Online Retail Dataset**, which contains transactional data from a UK-based online retail company.

### Important Columns

* InvoiceNo
* StockCode
* Description
* Quantity
* InvoiceDate
* UnitPrice
* CustomerID
* Country

---

## Data Preprocessing

The preprocessing module performs the following operations:

* Removes missing values
* Removes duplicate records
* Converts InvoiceDate to datetime format
* Removes cancelled transactions
* Removes invalid quantity and price values
* Creates TotalPrice feature
* Cleans data for further analysis

---

## Dashboard Modules

### Dashboard

Displays:

* Dataset overview
* Dataset statistics
* Business KPIs
* Cleaned dataset preview

---

### Visualizations

Interactive charts including:

* Revenue Trend
* Country-wise Sales
* Top Products
* Customer Distribution
* Revenue Distribution

---

### Customer Segmentation

Uses **RFM Analysis** to classify customers based on:

* **Recency** – How recently the customer purchased
* **Frequency** – How often the customer purchases
* **Monetary** – How much the customer spends

This helps identify:

* Best Customers
* Loyal Customers
* At-Risk Customers
* Lost Customers

---

### SQL Dashboard

Allows users to execute SQL queries on the processed dataset.

Example:

```sql
SELECT *
FROM transactions
LIMIT 10;
```

---

### Reports

Generate a PDF report summarizing key business insights and download it directly from the application.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/customer-purchase-analytics.git
```

### Move into the project directory

```bash
cd customer-purchase-analytics
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Application Workflow

1. Load the Online Retail dataset.
2. Preprocess and clean the data.
3. Store processed data in SQLite.
4. Display business KPIs.
5. Generate interactive visualizations.
6. Perform RFM customer segmentation.
7. Execute SQL queries.
8. Generate downloadable PDF reports.

---

## Future Enhancements

* User dataset upload support
* Machine Learning-based customer churn prediction
* Sales forecasting
* Product recommendation system
* Interactive filtering options
* Export visualizations as images
* User authentication
* Cloud deployment

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Business Intelligence Dashboards
* Customer Segmentation
* SQL Analytics
* Data Visualization
* PDF Report Generation
* Streamlit Web Application Development
* Python Data Analysis

---

## Author

**Amitoj Singh**

B.Tech Computer Science & Technology

Maharaja Agrasen Institute of Technology (MAIT)

---

