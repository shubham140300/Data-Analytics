import mysql.connector
import pandas as pd

# ==========================
# Connect to MySQL Database
# ==========================
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="poswal@123",      # Replace with your password if needed
    database="enterprise_compliance_db"
)

print("✅ Connected Successfully!\n")

# ==========================
# Load Tables into Pandas
# ==========================
servers = pd.read_sql("SELECT * FROM servers", connection)

compliance = pd.read_sql(
    "SELECT * FROM compliance",
    connection
)

performance = pd.read_sql(
    "SELECT * FROM performance",
    connection
)

vulnerabilities = pd.read_sql(
    "SELECT * FROM vulnerabilities",
    connection
)

incidents = pd.read_sql(
    "SELECT * FROM incidents",
    connection
)

# ==========================
# Check Shape
# ==========================
print("Dataset Shapes")
print("-" * 40)

print("Servers         :", servers.shape)
print("Compliance      :", compliance.shape)
print("Performance     :", performance.shape)
print("Vulnerabilities :", vulnerabilities.shape)
print("Incidents       :", incidents.shape)

# ==========================
# Display First 5 Rows
# ==========================
print("\n")
print("=" * 70)
print("SERVERS TABLE")
print("=" * 70)
print(servers.head())

print("\n")
print("=" * 70)
print("COMPLIANCE TABLE")
print("=" * 70)
print(compliance.head())

print("\n")
print("=" * 70)
print("PERFORMANCE TABLE")
print("=" * 70)
print(performance.head())

print("\n")
print("=" * 70)
print("VULNERABILITIES TABLE")
print("=" * 70)
print(vulnerabilities.head())

print("\n")
print("=" * 70)
print("INCIDENTS TABLE")
print("=" * 70)
print(incidents.head())

# ==========================
# Close Connection
# ==========================
connection.close()

print("\n")
print("✅ MySQL Connection Closed.")