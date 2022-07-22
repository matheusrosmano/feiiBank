import re

from pydantic import BaseModel, validator


class UserModelSerializer(BaseModel):
    name: str
    username: str
    cpf: str
    email: str
    password: str

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

