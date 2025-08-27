import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

def train():
    df = pd.read_csv("data/processed.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Corrected line: removed use_label_encoder=False
    model = XGBClassifier(eval_metric="logloss")
    
    model.fit(X_train, y_train)
    joblib.dump(model, "model.pkl")
    print("✅ Model trained -> model.pkl")

if __name__ == "__main__":
    train()