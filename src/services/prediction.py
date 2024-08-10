from io import BytesIO

import numpy as np
from PIL import Image
from tensorflow import keras

from src.ml.models import Model
from src.utils.singleton import Singleton


class Prediction(Singleton):

    def __init__(self):
        self.model = Model.instance().model

    def pre_process(self, image_input):
        img = Image.open(BytesIO(image_input.file.read()))
        img = img.resize((200, 200))
        x = keras.preprocessing.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        return images

    def predict(self, input_img):
        processed_input = self.pre_process(input_img)
        res = self.model.predict(processed_input)
        if res == 0:
            return "clean water"
        else:
            return "polluted water"
