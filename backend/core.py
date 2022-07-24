from typing import List

from sqlmodel import select

from backend.models import UserModel
from backend.database import get_session


def get_users() -> List[UserModel]:
    """Retorna os usuários do sistema"""
    with get_session() as session:
        sql = select(UserModel)
        return list(session.exec(sql))