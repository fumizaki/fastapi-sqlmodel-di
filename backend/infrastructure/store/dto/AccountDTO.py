# python standard library
from datetime import datetime, timedelta, timezone
# python external library
from sqlmodel import Field, SQLModel
# domain
from domain.entity.Account import Account
# presentation
from presentation.schema.view_model.SignUpViewModel import SignUpViewModel


class AccountDTO(SQLModel, table=True):

    __tablename__ = 'account'
    __table_args__ = {'extend_existing': True}
    id: str = Field(primary_key=True)
    email: str = Field(nullable=False)
    password: str = Field(nullable=False)


    def convert(self):
        return Account(
            id = self.id,
            email = self.email,
            password = self.password,
            )


    def set(self):
        return SignUpViewModel(
            id = self.id
            )


    @staticmethod
    def map(o: Account):
        return AccountDTO(
            id = o.id,
            email = o.email,
            password = o.password,
        )