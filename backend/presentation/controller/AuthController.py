# python external library
from fastapi import Depends
# presentation
from presentation.controller.AbsController import AbsController
from presentation.schema.form_object.SignUpFormObject import SignUpFormObject
# application
from application.usecase.SignUpUseCase import SignUpUseCase
# infrastructure
from infrastructure.utility.EntryPoint import EntryPoint
from infrastructure.utility.DI import DI



class AuthController(AbsController):

    def __init__(self):
        super().__init__()


        @self.router.post(EntryPoint.SIGN_UP)
        async def sign_up(form_object: SignUpFormObject, sign_up_usecase: SignUpUseCase = Depends(DI.sign_up)):
            try:
                result = sign_up_usecase.sign_up_exec(form_object)

            except:
                pass
