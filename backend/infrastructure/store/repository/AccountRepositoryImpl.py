# python external library
from sqlmodel import Session, select
from pydantic import EmailStr
# domain
from domain.repository.AccountRepository import AccountRepository
from domain.entity.Account import Account
# infrastructure
from infrastructure.store.dto.AccountDTO import AccountDTO

class AccountRepositoryImpl(AccountRepository):

    def __init__(self, session: Session):
        self.session = session


    def create(self, account: Account):
        try:
            dto = AccountDTO.map(account)
            self.session.add(dto)
            self.session.flush()

        except:
            raise


    def find_by_id(self, id: str):
        try:
            query = select(AccountDTO).where(AccountDTO.id==id)
            result = self.session.exec(query).one_or_none()
            return result

        except Exception as e:
            print(e)
            raise


    def find_by_email(self, email: EmailStr):
        try:
            query = select(AccountDTO).where(AccountDTO.email==email)
            result = self.session.exec(query).one_or_none()
            return result

        except Exception as e:
            print(e)
            raise