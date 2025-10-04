from pydantic import BaseModel, EmailStr, Field


class Author(BaseModel):
    name: str = Field(min_length=3, max_length=15)
    email: EmailStr


class Message(BaseModel):
    id: int = Field(..., gt=0)
    content: str = Field(min_length=1, max_length=500, pattern=r"[a-zA-Z\s!,.?]*$")
    author: Author
    tags: list[str] | None = Field(default=None)
    priority: float = Field(default=0.0, ge=0.0, le=10.0)
