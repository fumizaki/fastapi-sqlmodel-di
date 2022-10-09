# presentation
from presentation.schema.form_object.SignUpFormObject import SignUpFormObject
# application
from application.usecase.SignUpUseCase import SignUpUseCase
from application.transaction.SignUpTransaction import SignUpTransaction
# infrastructure
from infrastructure.utility.SomeId import SomeId
# domain
from domain.entity.Account import Account

class SignUpUseCaseImpl(SignUpUseCase):

    def __init__(self, transaction: SignUpTransaction):
        self.transaction: SignUpTransaction = transaction


    def sign_up_exec(self, form_object: SignUpFormObject):
        try:
            account_in_db = self.transaction.account_repository.find_by_email(form_object.email)

            if account_in_db is not None:
                raise

            sign_up_account = Account(
                id = SomeId.create_ulid(),
                email = form_object.email,
                password = form_object.password
            )

            self.transaction.account_repository.create(sign_up_account)

            self.transaction.commit()


        except:
            self.transaction.rollback()
            raise

