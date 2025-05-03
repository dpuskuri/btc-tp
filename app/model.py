from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    features = df[["volume", "vol_ma", "volume_spike", "consolidation"]]
    labels = df["target"]
    model = RandomForestClassifier()
    model.fit(features, labels)
    joblib.dump(model, "models/model.pkl")
