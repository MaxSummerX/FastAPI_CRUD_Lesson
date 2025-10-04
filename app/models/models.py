from pydantic import BaseModel, EmailStr


class Author(BaseModel):
    name: str
    email: EmailStr


class Message(BaseModel):
    id: int
    content: str
    author: Author
    tags: list[str] | None = None
    priority: int = 0
