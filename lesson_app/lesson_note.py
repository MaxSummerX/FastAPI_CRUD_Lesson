from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()

# Напишите здесь вашу модель.


class Note(BaseModel):
    id: int
    text: str


notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу"),
]

# Напишите здесь ваше решение.


@app.delete("/notes/{note_id}", response_model=Note, status_code=status.HTTP_200_OK)
async def delete_user(note_id: int) -> Note:
    for i, note in enumerate(notes):
        if note.id == note_id:
            delete_note = notes.pop(i)
            return delete_note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
