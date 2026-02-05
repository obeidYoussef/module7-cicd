from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from app.utils.logger import get_logger
from app.utils.exception import InvalidInputError

logger = get_logger(__name__)

MODEL_PATH = "app/models/trained_model.pkl"

logger = get_logger(__name__)

def train_model():
    try:
        # Load dataset
        iris = load_iris()
        X, y = iris.data, iris.target

        # Split dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the model
        model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Save the trained model to a file
        joblib.dump(model, MODEL_PATH)
        logger.info(f'Model trained and saved at {MODEL_PATH}')

    except Exception as e:
        logger.error(f'An error occurred during model training: {e}')


def load_model():
    model = joblib.load(MODEL_PATH)
    return model

def predict(input_data):
    if len(input_data[0]) < 4 or len(input_data[0]) != 4:
        logger.error("Invalid input data format. Expected a list of four numerical features.")
        raise InvalidInputError("Input data must be a list of four numerical features.")

    try:
        model = load_model()
        predictions = model.predict(input_data)
        return predictions
    
    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")