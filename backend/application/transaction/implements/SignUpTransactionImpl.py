# python external library
from sqlmodel import Session
# application
from application.transaction.SignUpTransaction import SignUpTransaction
# domain
from domain.repository.AccountRepository import AccountRepository

class SignUpTransactionImpl(SignUpTransaction):

    def __init__(self, session: Session, account_repository: AccountRepository):
        self.session = session
        self.account_repository = account_repository


    def begin(self):
        self.session.begin()


    def commit(self):
        self.session.commit()


    def rollback(self):
        self.session.rollback()


    def close(self):
        self.session.close()