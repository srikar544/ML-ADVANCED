import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import warnings

# Optional: suppress any minor UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

def train():
    # Load processed dataset
    df = pd.read_csv("data/processed.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Initialize model
    model = XGBClassifier(
        eval_metric="logloss",   # avoids deprecated use_label_encoder warning
        random_state=42,         # reproducible results
        n_jobs=-1                # use all CPU cores
    )
    
    # Train model
    model.fit(X_train, y_train)
    
    # Save trained model
    joblib.dump(model, "model.pkl")
    print("✅ Model trained -> model.pkl")

if __name__ == "__main__":
    train()
