import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI()

class InputData(BaseModel):
    feature_0: float
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float

@app.post("/predict")
def predict(data: InputData):
    X = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}
