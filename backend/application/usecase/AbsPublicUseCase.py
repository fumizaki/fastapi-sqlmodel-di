# python standard library
from abc import ABC, abstractmethod
# infrastructure
from infrastructure.utility.Logging import Logging

class AbsPublicUseCase(ABC):

    def __init__(self):
        self.logger = Logging.get(module = self.__class__.__name__)