from fastapi import APIRouter, HTTPException, status

from app.models.models import User, UserCreate, UserUpdate


router = APIRouter()

users = [
    User(id=1, name="Алексей", age=25),
    User(id=2, name="Мария", age=30),
    User(id=3, name="Иван", age=22),
    User(id=4, name="Елена", age=28),
    User(id=5, name="Дмитрий", age=35),
]


@router.get("/users", response_model=list[User], status_code=status.HTTP_201_CREATED, tags=["users"])
async def read_users() -> list[User]:
    return users


@router.get("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=["users"])
async def read_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, tags=["users"])
async def update_user(user_id: int, user: UserUpdate) -> User:
    for i, usr in enumerate(users):
        if usr.id == user_id:
            new_user = User(id=usr.id, name=user.name, age=user.age)
            users[i] = new_user
            return new_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED, tags=["users"])
async def create_user(user: UserCreate) -> User:
    next_id = max((usr.id for usr in users), default=-1) + 1
    new_user = User(id=next_id, name=user.name, age=user.age)
    users.append(new_user)
    return new_user
