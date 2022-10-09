# python standard library
import re
# python external library
from pydantic import BaseModel, validator


class Password(BaseModel):
    password: str

    @validator('password')
    def validate_password(cls, value):

        # 英大文字、英小文字、数字がそれぞれ1つ以上含まれていて、英数のみ8文字以上
        PASSWORD_REGEX = re.compile(
                r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}'
            )
        if not PASSWORD_REGEX.match(value):
            raise ValueError("Password: {} is incorrect".format(value))

        return value