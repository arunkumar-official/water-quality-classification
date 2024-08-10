import logging
import pickle
import traceback
from json import JSONDecodeError

from loguru import logger

from src.config.app_config import water_model_path
from src.utils.singleton import Singleton


class Model(Singleton):

    def __init__(self):
        try:
            with open(water_model_path, "rb") as f:
                self.model = pickle.load(f)
            logger.info("model loaded successfully")
        except FileNotFoundError:
            raise Exception("model is not found in given path")
        except JSONDecodeError:
            raise Exception("invalid json format in a file")
        except Exception as e:
            logging.error(e)
            traceback.print_exc(e)
            raise Exception("unknown exception raised")

# Model()
