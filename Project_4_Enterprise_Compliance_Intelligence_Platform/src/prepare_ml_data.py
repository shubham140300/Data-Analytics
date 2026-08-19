import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
# ==========================================
# Load Engineered Dataset
# ==========================================

data_path = "Enterprise_Compliance_Intelligence_Platform/data/master_dataset.csv"

df = pd.read_csv(data_path)

print("Dataset Loaded Successfully")

print("\nDataset Shape:")
print(df.shape)

print("\nAll Columns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())
# ==========================================
# Create Target Variable
# ==========================================

df["high_risk"] = (df["server_risk_score"] >= 70).astype(int)

print("\nTarget Variable Created")

print("\nHigh Risk Distribution:")
print(df["high_risk"].value_counts())

print("\nHigh Risk Percentage:")
print(df["high_risk"].value_counts(normalize=True) * 100)

# ==========================================
# Separate Features and Target
# ==========================================

y = df["high_risk"]

# Columns that should NOT be given to the ML model
leakage_columns = [
    "high_risk",
    "server_risk_score",
    "vulnerability_risk_score",
    "compliance_failure_count",
    "performance_risk_count",
    "incident_severity_score",
    "resolution_delay_risk"
]

X = df.drop(columns=leakage_columns)

print("\nFeatures and Target Separated Successfully")

print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)

print("\nFeatures Available:")
print(X.columns.tolist())
# ==========================================
# Remove Identifier and Date Columns
# ==========================================

columns_to_remove = [
    "server_id",
    "hostname",
    "compliance_id",
    "performance_id",
    "vulnerability_id",
    "incident_id",
    "created_date",
    "last_scan_date",
    "incident_date"
]

X = X.drop(columns=columns_to_remove)

print("\nIdentifier and Date Columns Removed")

print("\nX Shape After Removing Columns:")
print(X.shape)

print("\nRemaining Features:")
print(X.columns.tolist())
# ==========================================
# Identify Numerical and Categorical Features
# ==========================================

numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

print("\nNumerical Features:")
print(numerical_features)

print("\nNumber of Numerical Features:")
print(len(numerical_features))

print("\nCategorical Features:")
print(categorical_features)

print("\nNumber of Categorical Features:")
print(len(categorical_features))

# ==========================================
# Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split Completed")

print("\nX_train Shape:")
print(X_train.shape)

print("\nX_test Shape:")
print(X_test.shape)

print("\ny_train Shape:")
print(y_train.shape)

print("\ny_test Shape:")
print(y_test.shape)

print("\nTraining Target Distribution:")
print(y_train.value_counts(normalize=True) * 100)

print("\nTesting Target Distribution:")
print(y_test.value_counts(normalize=True) * 100)
# ==========================================
# Create Preprocessing Pipeline
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_features),

        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

print("\nPreprocessor Created Successfully")