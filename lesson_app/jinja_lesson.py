from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr


app = FastAPI()
templates = Jinja2Templates(directory="lesson_app/templates")


class User(BaseModel):
    name: str
    age: int
    status: bool
    data: dict
    email: EmailStr


@app.get("/")
def read_root(request: Request):
    user = User(
        name="Alice",
        age=19,
        status=True,
        data={"city": "Moscow", "tags": ["home", "work", "FastAPI", "pydantic", "jinja2"]},
        email="alice@example.com",
    )
    return templates.TemplateResponse("lesson_index.html", {"request": request, "user": user})
