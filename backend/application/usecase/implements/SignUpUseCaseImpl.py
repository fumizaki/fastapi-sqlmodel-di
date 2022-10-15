# presentation
from presentation.schema.form_object.SignUpFormObject import SignUpFormObject
from presentation.schema.view_model.GetAccountViewModel import GetAccountViewModel
# application
from application.usecase.SignUpUseCase import SignUpUseCase
from application.transaction.SignUpTransaction import SignUpTransaction
# infrastructure
from infrastructure.utility.SomeId import SomeId
# domain
from domain.entity.Account import Account

class SignUpUseCaseImpl(SignUpUseCase):

    def __init__(self, transaction: SignUpTransaction):
        super().__init__()
        self.transaction: SignUpTransaction = transaction


    def sign_up_exec(self, form_object: SignUpFormObject):
        try:
            account_in_db = self.transaction.account_repository.find_by_email(form_object.email)

            if account_in_db is not None:
                self.logger.info('Account is already exists: {}'.format(form_object.email))
                raise

            id = SomeId.create_ulid()

            sign_up_account = Account(
                id = id,
                email = form_object.email,
                password = form_object.password
            )

            self.transaction.account_repository.create(sign_up_account)
            self.transaction.commit()

            return GetAccountViewModel(
                id = id
            )

        except:
            self.transaction.rollback()
            raise


        finally:
            self.transaction.close()

