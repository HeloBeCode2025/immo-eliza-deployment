from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pycaret
from pycaret.datasets import get_data
from pycaret.regression import *
import pandas as pd


"""
df = pd.read_csv("my_data.csv")

setup(
    data=df,
    target="price",
)
"""

data = get_data("insurance")
s = setup(data, target = "charges")
best = compare_models()

#create_api (best, 'insurance_prediction_model')
save_model(best, "insurance_prediction_model")
#model = load_model('my_lr_api')

app = FastAPI()

model = load_model("insurance_prediction_model")

class InsuranceInput(BaseModel):
    age: int
    bmi: float
    children: int
    smoker: str
    region: str
    sex: str



class InsuranceOutput(BaseModel):
    prediction: float

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Insurance API is running"}


@app.post("/predict", response_model=InsuranceOutput)
def predict(data: InsuranceInput):
    df = pd.DataFrame([data.dict()])
    preds = predict_model(model, data=df)
    return InsuranceOutput(prediction=float(preds["prediction_label"].iloc[0]))


"""
app = FastAPI()

class Item(BaseModel):
    name : str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q": q}

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

"""