from fastapi import FastAPI

from src.routers import prediction_route
from src.services.prediction import Prediction
from src.ml.models import Model


app = FastAPI()

app.include_router(prediction_route.app)

@app.on_event("startup")
def init():
    Model.instance()
    Prediction.instance()