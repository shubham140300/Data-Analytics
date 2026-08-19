import mysql.connector
import pandas as pd

# =====================================
# Connect to MySQL
# =====================================
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="poswal@123",
    database="enterprise_compliance_db"
)

print("✅ Connected Successfully!\n")

# =====================================
# Load Tables
# =====================================
servers = pd.read_sql("SELECT * FROM servers", connection)
compliance = pd.read_sql("SELECT * FROM compliance", connection)
performance = pd.read_sql("SELECT * FROM performance", connection)
vulnerabilities = pd.read_sql("SELECT * FROM vulnerabilities", connection)
incidents = pd.read_sql("SELECT * FROM incidents", connection)

# =====================================
# Function to Analyze a DataFrame
# =====================================
def analyze_dataframe(df, table_name):

    print("\n" + "=" * 80)
    print(f"{table_name.upper()} TABLE")
    print("=" * 80)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

# =====================================
# Analyze Each Table
# =====================================

analyze_dataframe(servers, "Servers")

analyze_dataframe(compliance, "Compliance")

analyze_dataframe(performance, "Performance")

analyze_dataframe(vulnerabilities, "Vulnerabilities")

analyze_dataframe(incidents, "Incidents")

# ==========================================
# Business Analysis
# ==========================================

print("\n" + "=" * 80)
print("SERVER DISTRIBUTION BY ENVIRONMENT")
print("=" * 80)

environment_counts = servers["environment"].value_counts()

print(environment_counts)

connection.close()

print("\n✅ Analysis Completed")