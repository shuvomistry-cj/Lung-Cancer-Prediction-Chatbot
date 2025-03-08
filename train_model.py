import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("survey lung cancer.csv")

# Convert categorical values to numeric
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = LabelEncoder().fit_transform(df[col])

# Features & target
X = df.drop(columns=["LUNG_CANCER"])  # Independent variables
y = df["LUNG_CANCER"]  # Target variable (1 = High Risk, 0 = Low Risk)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open("../saved_model/lung_cancer_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model training complete! Model saved as 'lung_cancer_model.pkl'")
