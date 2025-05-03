import joblib
import pandas as pd

def predict(df):
    model = joblib.load("models/model.pkl")
    features = df[["volume", "vol_ma", "volume_spike", "consolidation"]].tail(1)
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][prediction]
    return {"trend": "up" if prediction == 1 else "down", "confidence": round(prob, 2)}
