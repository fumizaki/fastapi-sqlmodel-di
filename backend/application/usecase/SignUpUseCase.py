# python standard library
from abc import ABC, abstractmethod
# presentation
from presentation.schema.form_object.SignUpFormObject import SignUpFormObject

class SignUpUseCase(ABC):

    @abstractmethod
    def sign_up_exec(self, form_object: SignUpFormObject):
        raise NotImplementedError