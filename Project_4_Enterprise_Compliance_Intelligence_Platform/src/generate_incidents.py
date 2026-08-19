import pandas as pd
import random
from datetime import date, timedelta

# ---------------------------------------
# Read Server Data
# ---------------------------------------

servers_df = pd.read_csv("data/servers.csv")

# ---------------------------------------
# Store Incident Records
# ---------------------------------------

incident_records = []

# ---------------------------------------
# Incident Categories
# ---------------------------------------

incident_categories = [
    "Server Down",
    "CPU Utilization High",
    "Disk Space Full",
    "Memory Utilization High",
    "Splunk Agent Down",
    "Qualys Agent Missing",
    "CrowdStrike Offline",
    "Firewall Disabled",
    "Patch Failure",
    "Application Not Responding"
]

# ---------------------------------------
# Generate Incidents
# ---------------------------------------

for index, server in servers_df.iterrows():

    priority = random.choices(
        ["P1", "P2", "P3", "P4"],
        weights=[5, 15, 40, 40]
    )[0]

    status = random.choices(
        ["Open", "In Progress", "Resolved", "Closed"],
        weights=[10, 15, 35, 40]
    )[0]

    category = random.choice(incident_categories)

    assigned_team = server["owner_team"]

    if priority == "P1":
        resolution_hours = random.randint(1, 4)

    elif priority == "P2":
        resolution_hours = random.randint(2, 8)

    elif priority == "P3":
        resolution_hours = random.randint(4, 24)

    else:
        resolution_hours = random.randint(8, 72)

    incident_date = date.today() - timedelta(
        days=random.randint(0, 365)
    )

    incident = {

        "incident_id": index + 1,

        "server_id": server["server_id"],

        "incident_category": category,

        "priority": priority,

        "status": status,

        "assigned_team": assigned_team,

        "resolution_hours": resolution_hours,

        "incident_date": incident_date

    }

    incident_records.append(incident)

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

incident_df = pd.DataFrame(incident_records)

# ---------------------------------------
# Save CSV
# ---------------------------------------

incident_df.to_csv(
    "data/incidents.csv",
    index=False
)

# ---------------------------------------
# Display Output
# ---------------------------------------

print(incident_df.head(20))

print("\nTotal Incident Records :", len(incident_df))

print("Incidents CSV Created Successfully!")