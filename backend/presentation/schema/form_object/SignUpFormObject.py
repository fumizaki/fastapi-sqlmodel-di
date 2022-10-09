# presentation
from presentation.schema.value_object.Email import Email
from presentation.schema.value_object.Password import Password

class SignUpFormObject(Email, Password):
    pass