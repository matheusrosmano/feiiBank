from fastapi import FastAPI, Response, status
from backend.database import get_session
from backend.models import UserModel
from backend.serializers import UserModelSerializer

app = FastAPI(title='FeiiBank')


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
