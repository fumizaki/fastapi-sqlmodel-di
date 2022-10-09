# python standard library
from abc import ABC, abstractmethod
# python external library
from pydantic import EmailStr
# domain
from domain.entity.Account import Account



class AccountRepository(ABC):

    @abstractmethod
    def create(self, account: Account):
        raise NotImplementedError


    @abstractmethod
    def find_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: EmailStr):
        raise NotImplementedError

