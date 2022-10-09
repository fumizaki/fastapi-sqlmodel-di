# python standard library
from datetime import datetime, timedelta, timezone
from typing import Optional
# python external library
from pydantic import EmailStr

class Account:

    def __init__(
        self,
        id: str,
        email: EmailStr,
        password: str,
    ):
        self.id = id
        self.email = email
        self.password = password