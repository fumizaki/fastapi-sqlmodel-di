# python external library
from fastapi import APIRouter
# infrastructure
from infrastructure.utility.Logging import Logging

class AbsController:

    def __init__(self):
        self.router = APIRouter()
        self.logger = Logging.get(module=self.__class__.__name__)