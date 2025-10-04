from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


# Напишите здесь вашу модель.
class User(BaseModel):
    id: int
    name: str
    email: str


users = [
    User(id=1, name="Алексей", email="alexey@example.com"),
    User(id=2, name="Мария", email="maria@example.com"),
    User(id=3, name="Иван", email="ivan@example.com"),
    User(id=4, name="Елена", email="elena@example.com"),
    User(id=5, name="Дмитрий", email="dmitry@example.com"),
]

# Напишите здесь ваше решение.


@app.get("/users/{user_id}", response_model=User, status_code=status.HTTP_201_CREATED, tags=["users"])
async def read_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
