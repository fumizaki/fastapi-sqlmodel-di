# python standard library
from abc import abstractmethod, ABC

class AbsDatabase(ABC):

    _instance = {}

    def __new__(cls, database_url):
        """_summary_
            database_urlごとにシングルトンで実装
        """
        if cls._instance.get(database_url) is None:
            cls._instance[database_url] = super().__new__(cls)
        return cls._instance.get(database_url)

    @abstractmethod
    def get_engine():
        raise NotImplementedError