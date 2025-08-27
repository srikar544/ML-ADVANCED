import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

def evaluate():
    df = pd.read_csv("data/processed.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    model = joblib.load("model.pkl")
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print(f"✅ Model accuracy: {acc:.4f}")

if __name__ == "__main__":
    evaluate()
