# train_model.py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train():
    # 1. Load the dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Map target numbers to names for easier interpretation later
    target_names = iris.target_names

    # 2. Split the data (Optional: for verification)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Initialize and train the Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Check accuracy
    predictions = rf_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model trained with accuracy: {accuracy:.2f}")

    # 4. Save the model and the class names
    joblib.dump(rf_model, 'iris_model.pkl')
    joblib.dump(target_names, 'iris_classes.pkl')
    print("Model and class names saved to disk.")

if __name__ == "__main__":
    train()