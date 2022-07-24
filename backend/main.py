from typing import List

from fastapi import FastAPI, Response, status, HTTPException
from sqlmodel import select
from backend.core import get_users

from backend.database import get_session
from backend.models import UserModel
from backend.serializers import UserModelSerializer

app = FastAPI(title='FeiiBank', version=1.0, description='Uma api criada com o intuito de auxiliar clientes do feiibank')

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/users', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def add_users(users: UserModelSerializer, response: Response) -> UserModel:
    """Add a user into database"""
    user = UserModel(**users.dict())

    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

@app.get('/users', response_model=List[UserModel], status_code=status.HTTP_200_OK)
def list_users():
    """Get a list of users """
    users = get_users()
    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Users not found'
        )
    return users
