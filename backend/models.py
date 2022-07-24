from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class UserModel(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    username: str
    cpf: str
    email: str
    password: str
    date_create: datetime = Field(default_factory=datetime.now)
