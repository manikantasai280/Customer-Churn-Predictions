from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "churn_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_churn(customer_data):
    prediction = model.predict(customer_data)
    probability = model.predict_proba(customer_data)[0][1]

    return prediction[0], probability