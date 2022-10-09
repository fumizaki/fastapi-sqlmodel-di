# python external library
from fastapi import Depends
from sqlmodel import Session
# infrastructure
from infrastructure.utility.DBSession import DBSession
from infrastructure.store.repository.AccountRepositoryImpl import AccountRepositoryImpl
# application
from application.transaction.implements.SignUpTransactionImpl import SignUpTransactionImpl
from application.usecase.implements.SignUpUseCaseImpl import SignUpUseCaseImpl

class DI:

    def sign_up():
        session: Session = DBSession.get()
        account_repository = AccountRepositoryImpl(session)
        transaction = SignUpTransactionImpl(session, account_repository)
        return SignUpUseCaseImpl(transaction)

