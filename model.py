import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df_012 = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')

# Data preprocessing
X = df_012.drop('Diabetes_012', axis=1)  # Drop the target variable
y = df_012['Diabetes_012']               # Target variable (0: healthy, 1: prediabetic, 2: diabetic)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model as a .pkl file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")
