import mysql.connector
import pandas as pd


# ==========================================
# Connect to MySQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="poswal@123",
    database="enterprise_compliance_db"
)

print("✅ Connected to MySQL")


# ==========================================
# Load all tables
# ==========================================

servers = pd.read_sql(
    "SELECT * FROM servers",
    connection
)

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


print("\nTables loaded successfully.")

print("Servers:", servers.shape)
print("Compliance:", compliance.shape)
print("Performance:", performance.shape)
print("Vulnerabilities:", vulnerabilities.shape)
print("Incidents:", incidents.shape)

# ==========================================
# Merge Servers + Compliance
# ==========================================

master_df = pd.merge(
    servers,
    compliance,
    on="server_id",
    how="left"
)

print("\n✅ Servers + Compliance merged successfully")

print("\nMaster Dataset Shape:")
print(master_df.shape)

print("\nFirst 5 Rows:")
print(master_df.head())

print("\nColumns:")
print(master_df.columns.tolist())

# ==========================================
# Merge Performance
# ==========================================

master_df = pd.merge(
    master_df,
    performance,
    on="server_id",
    how="left"
)

print("\n✅ Performance merged successfully")

print("\nDataset Shape After Performance Merge:")
print(master_df.shape)

# ==========================================
# Merge Vulnerabilities
# ==========================================

master_df = pd.merge(
    master_df,
    vulnerabilities,
    on="server_id",
    how="left"
)

print("\n✅ Vulnerabilities merged successfully")

print("\nDataset Shape After Vulnerabilities Merge:")
print(master_df.shape)
# ==========================================
# Merge Incidents
# ==========================================

master_df = pd.merge(
    master_df,
    incidents,
    on="server_id",
    how="left"
)

print("\n✅ Incidents merged successfully")

print("\nDataset Shape After Incidents Merge:")
print(master_df.shape)

print("\nFinal Master Dataset - First 5 Rows:")
print(master_df.head())

print("\nFinal Master Dataset Columns:")
print(master_df.columns.tolist())

# ==========================================
# FEATURE ENGINEERING
# ==========================================

# Total vulnerabilities on each server
master_df["total_vulnerabilities"] = (
    master_df["critical_count"]
    + master_df["high_count"]
    + master_df["medium_count"]
    + master_df["low_count"]
)

print("\nTotal Vulnerabilities Feature Created")

print(
    master_df[
        [
            "server_id",
            "critical_count",
            "high_count",
            "medium_count",
            "low_count",
            "total_vulnerabilities"
        ]
    ].head()
)

# ==========================================
# Vulnerability Risk Score
# ==========================================

master_df["vulnerability_risk_score"] = (
    master_df["critical_count"] * 4
    + master_df["high_count"] * 3
    + master_df["medium_count"] * 2
    + master_df["low_count"]
)

print("\nVulnerability Risk Score Created")

print(
    master_df[
        [
            "server_id",
            "total_vulnerabilities",
            "vulnerability_risk_score"
        ]
    ].head()
)

# ==========================================
# Compliance Failure Count
# ==========================================

print("\nUnique values in compliance columns:")

compliance_columns = [
    "splunk_status",
    "qualys_status",
    "crowdstrike_status",
    "firewall_status",
    "patch_status",
    "password_policy"
]

for column in compliance_columns:
    print(column, master_df[column].unique())

# ==========================================
# Create Compliance Failure Count
# ==========================================

master_df["compliance_failure_count"] = (
    (master_df["splunk_status"] == "Stopped").astype(int)
    + (master_df["qualys_status"] == "Stopped").astype(int)
    + (master_df["crowdstrike_status"] == "Stopped").astype(int)
    + (master_df["firewall_status"] == "Disabled").astype(int)
    + (master_df["patch_status"] == "Outdated").astype(int)
    + (master_df["password_policy"] == "Non-Compliant").astype(int)
)

print("\nCompliance Failure Count Created")

print(
    master_df[
        [
            "server_id",
            "splunk_status",
            "qualys_status",
            "crowdstrike_status",
            "firewall_status",
            "patch_status",
            "password_policy",
            "compliance_failure_count"
        ]
    ].head()
)

# ==========================================
# Inspect Performance Metrics
# ==========================================

print("\nPerformance Metrics Summary:")

performance_columns = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "uptime_days"
]

print(master_df[performance_columns].describe())

# ==========================================
# Create Performance Risk Count
# ==========================================

master_df["performance_risk_count"] = (
    (master_df["cpu_usage"] > 80).astype(int)
    + (master_df["memory_usage"] > 80).astype(int)
    + (master_df["disk_usage"] > 85).astype(int)
    + (master_df["uptime_days"] > 600).astype(int)
)

print("\nPerformance Risk Count Created")

print(
    master_df[
        [
            "server_id",
            "cpu_usage",
            "memory_usage",
            "disk_usage",
            "uptime_days",
            "performance_risk_count"
        ]
    ].head(10)
)

# ==========================================
# Inspect Incident Data
# ==========================================

print("\nIncident Data Summary:")

print("\nPriority Values:")
print(master_df["priority"].value_counts())

print("\nIncident Status Values:")
print(master_df["status"].value_counts())

print("\nIncident Categories:")
print(master_df["incident_category"].value_counts())

print("\nResolution Hours Summary:")
print(master_df["resolution_hours"].describe())
# ==========================================
# Incident Severity Score
# ==========================================

priority_score_map = {
    "P1": 4,
    "P2": 3,
    "P3": 2,
    "P4": 1
}

master_df["incident_severity_score"] = (
    master_df["priority"].map(priority_score_map)
)

print("\nIncident Severity Score Created")

print(
    master_df[
        [
            "server_id",
            "incident_category",
            "priority",
            "incident_severity_score"
        ]
    ].head(10)
)
# ==========================================
# Resolution Delay Risk
# ==========================================

master_df["resolution_delay_risk"] = (
    master_df["resolution_hours"] > 24
).astype(int)

print("\nResolution Delay Risk Created")

print(
    master_df[
        [
            "server_id",
            "priority",
            "resolution_hours",
            "resolution_delay_risk"
        ]
    ].head(10)
)

# ==========================================
# Overall Server Risk Score
# ==========================================

master_df["server_risk_score"] = (
    master_df["vulnerability_risk_score"]
    + (master_df["compliance_failure_count"] * 10)
    + (master_df["performance_risk_count"] * 5)
    + (master_df["incident_severity_score"] * 5)
    + (master_df["resolution_delay_risk"] * 5)
)

print("\nOverall Server Risk Score Created")

print(
    master_df[
        [
            "server_id",
            "vulnerability_risk_score",
            "compliance_failure_count",
            "performance_risk_count",
            "incident_severity_score",
            "resolution_delay_risk",
            "server_risk_score"
        ]
    ].head(10)
)

# ==========================================
# Save Final Engineered Dataset
# ==========================================

output_path = "Enterprise_Compliance_Intelligence_Platform/data/master_dataset.csv"

master_df.to_csv(output_path, index=False)

print("\nFinal Engineered Dataset Saved Successfully")

print("\nFinal Dataset Shape:")
print(master_df.shape)

print("\nFinal Number of Columns:")
print(len(master_df.columns))