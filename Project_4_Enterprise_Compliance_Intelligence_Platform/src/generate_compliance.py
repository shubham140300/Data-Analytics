import pandas as pd
import random

# ---------------------------------------
# Read Server Data
# ---------------------------------------

servers_df = pd.read_csv("data/servers.csv")

# ---------------------------------------
# Store Compliance Records
# ---------------------------------------

compliance_records = []

# ---------------------------------------
# Generate Compliance Data
# ---------------------------------------

for index, server in servers_df.iterrows():

    # -----------------------------
    # Security Tool Status
    # -----------------------------

    splunk_status = random.choices(
        ["Running", "Stopped"],
        weights=[95, 5]
    )[0]

    qualys_status = random.choices(
        ["Running", "Stopped"],
        weights=[96, 4]
    )[0]

    crowdstrike_status = random.choices(
        ["Running", "Stopped"],
        weights=[97, 3]
    )[0]

    firewall_status = random.choices(
        ["Enabled", "Disabled"],
        weights=[98, 2]
    )[0]

    patch_status = random.choices(
        ["Updated", "Outdated"],
        weights=[90, 10]
    )[0]

    password_policy = random.choices(
        ["Compliant", "Non-Compliant"],
        weights=[92, 8]
    )[0]

    # -----------------------------
    # Calculate Compliance Score
    # -----------------------------

    score = 0

    if splunk_status == "Running":
        score += 20

    if qualys_status == "Running":
        score += 20

    if crowdstrike_status == "Running":
        score += 20

    if firewall_status == "Enabled":
        score += 15

    if patch_status == "Updated":
        score += 15

    if password_policy == "Compliant":
        score += 10

    # -----------------------------
    # Compliance Status
    # -----------------------------

    if score >= 90:
        compliance_status = "Compliant"

    elif score >= 70:
        compliance_status = "Warning"

    else:
        compliance_status = "Non-Compliant"

    # -----------------------------
    # Create Compliance Record
    # -----------------------------

    compliance = {
        "compliance_id": index + 1,
        "server_id": server["server_id"],
        "splunk_status": splunk_status,
        "qualys_status": qualys_status,
        "crowdstrike_status": crowdstrike_status,
        "firewall_status": firewall_status,
        "patch_status": patch_status,
        "password_policy": password_policy,
        "compliance_score": score,
        "compliance_status": compliance_status
    }

    compliance_records.append(compliance)

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

compliance_df = pd.DataFrame(compliance_records)

# ---------------------------------------
# Save CSV
# ---------------------------------------

compliance_df.to_csv("data/compliance.csv", index=False)

# ---------------------------------------
# Display Output
# ---------------------------------------

print(compliance_df.head(20))

print("\nTotal Compliance Records :", len(compliance_df))
print("Compliance CSV Created Successfully!")