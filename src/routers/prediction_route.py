import traceback

from fastapi import UploadFile, APIRouter, File

from src.services.prediction import Prediction

app = APIRouter(prefix="/predict")


@app.post("")
def get_image(file_input: UploadFile):
    try:
        res = Prediction.instance().predict(file_input)
        return {"prediction": res}
    except Exception as e:
        traceback.print_exc(e)
        return {"prediction error": str(e)}
