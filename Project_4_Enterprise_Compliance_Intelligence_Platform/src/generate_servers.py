import random
import pandas as pd
from datetime import date

# ---------------------------------------
# Master Lists
# ---------------------------------------

operating_systems = [
    "RHEL 8",
    "RHEL 9",
    "Windows Server 2019",
    "Windows Server 2022",
    "Ubuntu 22.04"
]

environments = [
    "Production",
    "Development",
    "Testing",
    "UAT"
]

locations = [
    "Mumbai",
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Chennai"
]

# ---------------------------------------
# Server Type Mapping
# ---------------------------------------

server_mapping = {
    "Web Server": "WEB",
    "Application Server": "APP",
    "Database Server": "DB",
    "File Server": "FILE",
    "API Server": "API",
    "Mail Server": "MAIL",
    "Authentication Server": "AUTH"
}

# ---------------------------------------
# Team Mapping
# ---------------------------------------

team_mapping = {
    "Web Server": "Linux Team",
    "Application Server": "Infrastructure Team",
    "Database Server": "Database Team",
    "File Server": "Windows Team",
    "API Server": "Infrastructure Team",
    "Mail Server": "Messaging Team",
    "Authentication Server": "Security Team"
}

# ---------------------------------------
# Hostname Counters
# ---------------------------------------

hostname_counter = {
    "WEB": 1,
    "APP": 1,
    "DB": 1,
    "FILE": 1,
    "API": 1,
    "MAIL": 1,
    "AUTH": 1
}

# ---------------------------------------
# Store Generated Data
# ---------------------------------------

servers = []

# ---------------------------------------
# Generate 5000 Servers
# ---------------------------------------

for server_id in range(1, 5001):

    server_type = random.choice(list(server_mapping.keys()))

    prefix = server_mapping[server_type]

    hostname = f"{prefix}{hostname_counter[prefix]:03}"

    hostname_counter[prefix] += 1

    owner_team = team_mapping[server_type]

    server = {
        "server_id": server_id,
        "hostname": hostname,
        "operating_system": random.choice(operating_systems),
        "environment": random.choice(environments),
        "server_type": server_type,
        "location": random.choice(locations),
        "owner_team": owner_team,
        "created_date": date.today()
    }

    servers.append(server)

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

df = pd.DataFrame(servers)

# ---------------------------------------
# Save CSV
# ---------------------------------------

df.to_csv("data/servers.csv", index=False)

print(df.head(20))

print("\nTotal Servers Generated :", len(df))
print("CSV Created Successfully!")