from pydantic import BaseModel, EmailStr, Field


class Author(BaseModel):
    name: str = Field(min_length=3, max_length=15)
    email: EmailStr


class Messages(BaseModel):
    id: int = Field(..., gt=0)
    content: str = Field(min_length=1, max_length=500, pattern=r"[a-zA-Z\s!,.?]*$")
    author: Author
    tags: list[str] | None = Field(default=None)
    priority: float = Field(default=0.0, ge=0.0, le=10.0)


# Модель для входных данных (запросов: создание и обновление)
class MessageCreate(BaseModel):
    content: str


# Модель для ответов и хранения в базе данных
class Message(BaseModel):
    id: int
    content: str


# Модель для создания задачи в базе данных
class Task(BaseModel):
    id: int
    title: str
    completed: bool


class UserCreate(BaseModel):
    name: str
    age: int = Field(..., ge=18)


class User(BaseModel):
    id: int
    name: str
    age: int = Field(..., ge=18)


class UserUpdate(BaseModel):
    name: str
    age: int = Field(..., ge=18)
