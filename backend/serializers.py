import re

from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class UserModelSerializer(BaseModel):
    """
    Classe usada para representar usuário

    Attributes
    --------------------
    name: str
        Nome do cliente

    username: str
        Nickname único que vai ser usado pelo cliente

    cpf: str
        CPF do cliente

    email: str
        Email do cliente

    password: str
        Senha do cliente
    """
    name: str
    username: str
    cpf: str
    email: str
    password: str

    @validator('cpf')
    def cpf_must_contain_caracter(cls, v, field):
        if len(v) != 11:
            raise HTTPException(
                detail=f'{field.name} is not valid',
                status_code=status.HTTP_412_PRECONDITION_FAILED
            )
        return v

    @validator('email')
    def email_is_valid(cls, v, field):
        if re.fullmatch('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', v) is None:
            raise HTTPException(
                detail=f'{field.name} is not valid',
                status_code=status.HTTP_412_PRECONDITION_FAILED
            )
        return v

