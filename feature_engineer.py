import pandas as pd
from sklearn.preprocessing import StandardScaler

def feature_engineer():
    df = pd.read_csv("data/raw.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    df_out = pd.DataFrame(X_scaled, columns=X.columns)
    df_out["target"] = y
    df_out.to_csv("data/processed.csv", index=False)
    print("✅ Features engineered -> data/processed.csv")

if __name__ == "__main__":
    feature_engineer()
