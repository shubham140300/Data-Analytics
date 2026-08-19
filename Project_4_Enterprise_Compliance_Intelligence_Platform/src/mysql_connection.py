import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="poswal@123",
    database="enterprise_compliance_db"
)

print("Connected Successfully!")

# Read table into DataFrame
query = "SELECT * FROM servers"

df = pd.read_sql(query, connection)

# Display first 5 rows
print(df.head())

# Close connection
connection.close()