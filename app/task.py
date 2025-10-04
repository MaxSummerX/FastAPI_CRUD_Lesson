from fastapi import APIRouter, status

from app.models.models import Task


router = APIRouter()

tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False),
]


@router.get("/tasks", response_model=list[Task], status_code=status.HTTP_200_OK, tags=["tasks"])
async def read_tasks() -> list[Task]:
    return tasks
