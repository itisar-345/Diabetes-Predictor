import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import gzip
from joblib import dump

# Load dataset
df_012 = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')

# Data preprocessing
X = df_012.drop('Diabetes_012', axis=1)  # Drop the target variable
y = df_012['Diabetes_012']               # Target variable (0: healthy, 1: prediabetic, 2: diabetic)

# Convert data to a smaller type (float32) to reduce memory usage
X = X.astype('float32')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest Classifier with optimized parameters
model = RandomForestClassifier(
    n_estimators=30,      
    random_state=42
)
model.fit(X_train, y_train)

# Save only the essential model attributes to reduce size
model_to_save = {
    "estimators_": model.estimators_,
    "classes_": model.classes_,
    "n_classes_": model.n_classes_
}

# Save the model with gzip compression
with gzip.open('model_compressed.pkl.gz', 'wb') as f:
    pickle.dump(model_to_save, f)

# Alternatively, save using joblib with compression
dump(model, 'model_compressed.joblib', compress=('gzip', 3)) 

print("Compressed model saved as model_compressed.pkl.gz and model_compressed.joblib")
