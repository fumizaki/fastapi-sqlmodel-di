# python external library
from sqlmodel import create_engine
# infrastructure
from infrastructure.module.AbsDatabase import AbsDatabase


class Database(AbsDatabase):

    def __init__(self, database_url):
        self.__database_url = database_url

    def get_engine(self):
        return create_engine(self.__database_url, echo=False)


