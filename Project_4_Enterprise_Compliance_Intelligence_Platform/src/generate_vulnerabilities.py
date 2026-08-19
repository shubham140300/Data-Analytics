import pandas as pd
import random
from datetime import date

# ---------------------------------------
# Read Server Data
# ---------------------------------------

servers_df = pd.read_csv("data/servers.csv")

# ---------------------------------------
# Store Vulnerability Records
# ---------------------------------------

vulnerability_records = []

# ---------------------------------------
# Generate Vulnerabilities
# ---------------------------------------

for index, server in servers_df.iterrows():

    server_type = server["server_type"]

    # ---------------------------------------
    # Vulnerability Logic
    # ---------------------------------------

    if server_type == "Database Server":

        critical = random.randint(0, 5)
        high = random.randint(2, 10)
        medium = random.randint(5, 20)
        low = random.randint(10, 30)

    elif server_type == "Web Server":

        critical = random.randint(0, 3)
        high = random.randint(1, 6)
        medium = random.randint(4, 15)
        low = random.randint(5, 20)

    elif server_type == "Application Server":

        critical = random.randint(0, 2)
        high = random.randint(1, 5)
        medium = random.randint(3, 12)
        low = random.randint(6, 18)

    elif server_type == "File Server":

        critical = random.randint(0, 1)
        high = random.randint(0, 3)
        medium = random.randint(2, 8)
        low = random.randint(5, 15)

    elif server_type == "API Server":

        critical = random.randint(0, 2)
        high = random.randint(1, 5)
        medium = random.randint(3, 10)
        low = random.randint(5, 15)

    elif server_type == "Mail Server":

        critical = random.randint(0, 2)
        high = random.randint(1, 4)
        medium = random.randint(2, 10)
        low = random.randint(5, 15)

    elif server_type == "Authentication Server":

        critical = random.randint(0, 2)
        high = random.randint(1, 4)
        medium = random.randint(2, 8)
        low = random.randint(4, 12)

    # ---------------------------------------
    # Risk Level
    # ---------------------------------------

    if critical >= 3:
        risk_level = "Critical"

    elif high >= 5:
        risk_level = "High"

    elif medium >= 8:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    # ---------------------------------------
    # Last Scan Date
    # ---------------------------------------

    last_scan_date = date.today()

    # ---------------------------------------
    # Create Vulnerability Record
    # ---------------------------------------

    vulnerability = {

        "vulnerability_id": index + 1,

        "server_id": server["server_id"],

        "critical_count": critical,

        "high_count": high,

        "medium_count": medium,

        "low_count": low,

        "risk_level": risk_level,

        "last_scan_date": last_scan_date

    }

    vulnerability_records.append(vulnerability)

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

vulnerability_df = pd.DataFrame(vulnerability_records)

# ---------------------------------------
# Save CSV
# ---------------------------------------

vulnerability_df.to_csv(
    "data/vulnerabilities.csv",
    index=False
)

# ---------------------------------------
# Display Output
# ---------------------------------------

print(vulnerability_df.head(20))

print("\nTotal Vulnerability Records :", len(vulnerability_df))

print("Vulnerabilities CSV Created Successfully!")