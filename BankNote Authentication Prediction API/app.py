from fastapi import FastAPI
import uvicorn
import pickle
from schemas import BankNote
import pandas as Pd
import numpy as np



app = FastAPI()
pickle_in = open("Banknote.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.post("/predict")
def predict_Banknote(data:BankNote): 
    # print(data)
    # data = data.dict()
    data = data.model_dump()
    # print(data)
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]
    prediction = classifier.predict([[variance,skewness,curtosis,entropy,]])
    if (prediction[0]>0.5):
        prediction = "Fake Note"
    else:
        prediction = "Authentic Note"
    return{"prediction": prediction}

if __name__ =="__main__":
    uvicorn.run(app, host="127.0.0.1",port = 8000)
    
