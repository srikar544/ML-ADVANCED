import pandas as pd
import numpy as np

def ingest_data():
    # Generate synthetic dataset
    np.random.seed(42)
    X = np.random.rand(1000, 5)
    y = (X[:, 0] + X[:, 1] * 2 + np.random.rand(1000) * 0.1 > 1).astype(int)
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(5)])
    df["target"] = y
    df.to_csv("data/raw.csv", index=False)
    print("✅ Data ingested -> data/raw.csv")

if __name__ == "__main__":
    ingest_data()
