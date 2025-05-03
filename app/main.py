from fastapi import FastAPI
from app.data_fetcher import fetch_data
from app.feature_engineering import add_features
from app.predictor import predict

app = FastAPI()

@app.get("/predict")
def get_prediction():
    df = fetch_data()
    df = add_features(df)
    result = predict(df)
    return result
