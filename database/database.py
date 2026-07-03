import sqlite3
import pandas as pd
def create_database(df):
    conn = sqlite3.connect("database/customer.db")
    df.to_sql(
        "transactions",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()
def run_query(query):
    conn = sqlite3.connect("database/customer.db")
    result = pd.read_sql(query, conn)
    conn.close()
    return result