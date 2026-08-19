import pandas as pd
import random

# ---------------------------------------
# Read Server Data
# ---------------------------------------

servers_df = pd.read_csv("data/servers.csv")

# ---------------------------------------
# Store Performance Records
# ---------------------------------------

performance_records = []

# ---------------------------------------
# Generate Performance Data
# ---------------------------------------

for index, server in servers_df.iterrows():

    server_type = server["server_type"]

    # ---------------------------------------
    # Generate Performance Based on Server Type
    # ---------------------------------------

    if server_type == "Web Server":

        cpu_usage = random.randint(20, 60)
        memory_usage = random.randint(30, 70)
        disk_usage = random.randint(20, 60)

    elif server_type == "Application Server":

        cpu_usage = random.randint(40, 80)
        memory_usage = random.randint(50, 85)
        disk_usage = random.randint(40, 75)

    elif server_type == "Database Server":

        cpu_usage = random.randint(60, 90)
        memory_usage = random.randint(70, 95)
        disk_usage = random.randint(65, 95)

    elif server_type == "File Server":

        cpu_usage = random.randint(10, 35)
        memory_usage = random.randint(20, 50)
        disk_usage = random.randint(70, 95)

    elif server_type == "API Server":

        cpu_usage = random.randint(45, 80)
        memory_usage = random.randint(40, 75)
        disk_usage = random.randint(30, 60)

    elif server_type == "Mail Server":

        cpu_usage = random.randint(25, 55)
        memory_usage = random.randint(40, 70)
        disk_usage = random.randint(30, 65)

    elif server_type == "Authentication Server":

        cpu_usage = random.randint(30, 60)
        memory_usage = random.randint(40, 70)
        disk_usage = random.randint(25, 55)

    # ---------------------------------------
    # Uptime
    # ---------------------------------------

    uptime_days = random.randint(1, 730)

    # ---------------------------------------
    # Create Performance Record
    # ---------------------------------------

    performance = {

        "performance_id": index + 1,

        "server_id": server["server_id"],

        "cpu_usage": cpu_usage,

        "memory_usage": memory_usage,

        "disk_usage": disk_usage,

        "uptime_days": uptime_days

    }

    performance_records.append(performance)

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

performance_df = pd.DataFrame(performance_records)

# ---------------------------------------
# Save CSV
# ---------------------------------------

performance_df.to_csv("data/performance.csv", index=False)

# ---------------------------------------
# Display Output
# ---------------------------------------

print(performance_df.head(20))

print("\nTotal Performance Records :", len(performance_df))

print("Performance CSV Created Successfully!")