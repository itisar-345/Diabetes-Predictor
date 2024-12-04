import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df_012 = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')

# Data preprocessing
X = df_012.drop('Diabetes_012', axis=1)  # Drop the target variable
y = df_012['Diabetes_012']               # Target variable (0: healthy, 1: prediabetic, 2: diabetic)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=30, random_state=42)
model.fit(X_train, y_train)

def plot_plan_random_forest_accuracy():
    # Simulated data for accuracies
    estimators_range = range(10, 101, 10)
    train_accuracies = np.linspace(0.85, 1.0, len(estimators_range))
    test_accuracies = np.linspace(0.75, 0.85, len(estimators_range))

    plt.figure(figsize=(10, 6))
    plt.plot(estimators_range, train_accuracies, label='Training Accuracy', color='blue', marker='o')
    plt.plot(estimators_range, test_accuracies, label='Testing Accuracy', color='green', marker='o')
    plt.title('Plan: Expected Random Forest Training and Testing Accuracy')
    plt.xlabel('Number of Trees (n_estimators)', fontsize=12)
    plt.ylabel('Accuracy', fontsize=12)
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

def visualize_accuracy_and_confusion_matrix(y_test, y_pred):
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Display the accuracy score
    print(f"Accuracy of the model: {accuracy * 100:.2f}%")

    # Confusion Matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False, annot_kws={"size": 16})
    plt.title('Confusion Matrix', fontsize=18)
    plt.ylabel('True Label', fontsize=14)
    plt.xlabel('Predicted Label', fontsize=14)
    plt.show()

    # Bar plot for Accuracy Visualization
    categories = ['Correct Predictions', 'Incorrect Predictions']
    values = [accuracy, 1 - accuracy]

    plt.figure(figsize=(6, 4))
    sns.barplot(x=categories, y=values, palette='viridis')
    plt.title('Model Prediction Accuracy', fontsize=16)
    plt.ylabel('Proportion', fontsize=12)
    plt.ylim(0, 1)
    for i, value in enumerate(values):
        plt.text(i, value + 0.02, f'{value * 100:.2f}%', ha='center', fontsize=12)
    plt.show()

def run_model_and_visualize(X_train, X_test, y_train, y_test):
    # Build and fit the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate and visualize the results
    visualize_accuracy_and_confusion_matrix(y_test, y_pred)

plot_plan_random_forest_accuracy()

run_model_and_visualize(X_train, X_test, y_train, y_test)

y_pred = model.predict(X_test)
class_report = classification_report(y_test, y_pred)

print("Classification Report:\n", class_report)

