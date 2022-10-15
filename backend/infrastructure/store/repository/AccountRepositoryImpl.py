# python external library
from sqlmodel import Session, select
from pydantic import EmailStr
# domain
from domain.repository.AccountRepository import AccountRepository
from domain.entity.Account import Account
# infrastructure
from infrastructure.store.dto.AccountDTO import AccountDTO
from infrastructure.utility.Logging import Logging

class AccountRepositoryImpl(AccountRepository):

    def __init__(self, session: Session):
        self.session = session
        self.logger = Logging.get(module=self.__class__.__name__)


    def create(self, account: Account):
        try:
            self.logger.info(account)
            dto = AccountDTO.map(account)
            self.session.add(dto)
            self.session.flush()

        except Exception as e:
            self.logger.error(e)
            raise


    def find_by_id(self, id: str):
        try:
            query = select(AccountDTO).where(AccountDTO.id==id)
            result = self.session.exec(query).one_or_none()
            return result

        except Exception as e:
            self.logger.error(e)
            raise


    def find_by_email(self, email: EmailStr):
        try:
            query = select(AccountDTO).where(AccountDTO.email==email)
            result = self.session.exec(query).one_or_none()
            return result

        except Exception as e:
            self.logger.error(e)
            raise