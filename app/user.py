from fastapi import APIRouter, status

from app.models.models import User, UserCreate


router = APIRouter()

users = []


@router.get("/users", response_model=list[User], status_code=status.HTTP_201_CREATED, tags=["users"])
async def read_users() -> list[User]:
    return users


@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED, tags=["users"])
async def create_user(user: UserCreate) -> User:
    next_id = max((usr.id for usr in users), default=-1) + 1
    new_user = User(id=next_id, name=user.name, age=user.age)
    users.append(new_user)
    return new_user
