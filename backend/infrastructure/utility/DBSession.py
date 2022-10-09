# python external library
from sqlmodel import Session
# infrastructure
from infrastructure.module.Database import Database


class DBSession:

    DB_URL = "sqlite:///../db/sqlite/sqlite.db"

    @classmethod
    def get(cls):

        db = Database(cls.DB_URL)
        session = Session(db.get_engine())

        # try:
        #     yield session
        # finally:
        #     session.close()
        #
        # ERROR: 'generator' object has no attribute 'exec'

        return session
