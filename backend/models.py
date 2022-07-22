import re
from typing import Optional
from pydantic import validator
from sqlmodel import SQLModel, Field
from datetime import datetime


class UserModel(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    username: str
    cpf: str
    email: str
    password: str
    date_create: datetime = Field(default_factory=datetime.now)


    @validator('cpf')
    def cpf_must_contain_caracter(cls, v, field):
        if len(v) != 11:
            raise RuntimeError(f'{field.name} is not valid')
        return v


    @validator('email')
    def email_is_valid(cls, v, field):
        if re.fullmatch('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', v) is None:
            raise RuntimeError(f'{field.name} is not valid')
        return v



teste = UserModel()
