# python standard library
from abc import ABC, abstractmethod
# domain
from domain.repository.AccountRepository import AccountRepository

class SignUpTransaction(ABC):

    account_repository: AccountRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError


    @abstractmethod
    def commit(self):
        raise NotImplementedError


    @abstractmethod
    def rollback(self):
        raise NotImplementedError