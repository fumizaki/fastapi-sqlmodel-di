# python standard library
import re
# python external library
from pydantic import BaseModel, EmailStr, validator

class Email(BaseModel):
    email: EmailStr


    @validator('email')
    def validate_email(cls, value):
        EMAIL_REGEX = re.compile(
            r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'
        )
        if not EMAIL_REGEX.match(value):
            raise ValueError("Email: {} is incorrect".format(value))

        return value