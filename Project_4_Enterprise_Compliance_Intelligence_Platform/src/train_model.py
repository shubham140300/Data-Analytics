import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
# ==========================================
# Load Master Dataset
# ==========================================

data_path = "data/master_dataset.csv"

df = pd.read_csv(data_path)

print("Dataset Loaded Successfully")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())
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

X = df.drop(columns=["high_risk"])

print("\nFeatures and Target Separated Successfully")

print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)
# ==========================================
# Remove Target Leakage
# ==========================================

leakage_columns = [
    "server_risk_score",
    "vulnerability_risk_score",
    "compliance_failure_count",
    "performance_risk_count",
    "incident_severity_score",
    "resolution_delay_risk",
    "risk_level"
]

X = X.drop(columns=leakage_columns)

print("\nTarget Leakage Columns Removed")

print("\nX Shape After Removing Leakage:")
print(X.shape)
# ==========================================
# Remove Identifier and Date Columns
# ==========================================

columns_to_remove = [
    "server_id",
    "hostname",
    "created_date",
    "last_scan_date",
    "incident_date",
    "incident_id",
    "vulnerability_id"
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

numerical_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

print("\nNumerical Features:")
print(numerical_features)

print("\nNumber of Numerical Features:")
print(len(numerical_features))

print("\nCategorical Features:")
print(categorical_features)

print("\nNumber of Categorical Features:")
print(len(categorical_features))
# ==========================================
# Create Preprocessing Pipeline
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

print("\nPreprocessor Created Successfully")
# ==========================================
# Create Machine Learning Pipeline
# ==========================================

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42
            )
        )
    ]
)

print("\nMachine Learning Pipeline Created Successfully")
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

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)
# ==========================================
# Train Model
# ==========================================

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Model Training Completed")
print("\nMaking Predictions...")

y_pred = model.predict(X_test)

print("Predictions Completed")

print("\nFirst 20 Predictions:")
print(y_pred[:20])

print("\nFirst 20 Actual Values:")
print(y_test.values[:20])
# ==========================================
# Model Evaluation
# ==========================================

print("\nModel Evaluation")

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================================
# Save Trained Model
# ==========================================

model_path = "models/logistic_regression_model.pkl"

joblib.dump(model, model_path)

print("\nModel Saved Successfully")
print("Model Path:", model_path)
# ==========================================
# Save Prediction Results
# ==========================================

prediction_results = X_test.copy()

prediction_results["actual_high_risk"] = y_test.values
prediction_results["predicted_high_risk"] = y_pred

prediction_results["high_risk_probability"] = model.predict_proba(X_test)[:, 1]

prediction_output_path = "data/ml_predictions.csv"

prediction_results.to_csv(
    prediction_output_path,
    index=False
)

print("\nPrediction Results Saved Successfully")
print("Prediction Output Path:", prediction_output_path)