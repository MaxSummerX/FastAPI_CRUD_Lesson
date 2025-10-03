from fastapi import APIRouter, Body, HTTPException, status


router = APIRouter()

notes_db = {0: "Study FastAPI", 1: "I like FastAPI"}


@router.get("/notes", tags=["notes"])
async def read_notes() -> dict[int, str]:
    if not notes_db:
        return {}
    return notes_db


@router.get("/notes/{note_id}", tags=["notes"])
async def read_note(note_id: int) -> str:
    try:
        return notes_db[note_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")


@router.post("/notes", status_code=status.HTTP_201_CREATED, tags=["notes"])
async def create_note(note: str = Body(...)) -> str:
    current_index = max(notes_db) + 1 if notes_db else 0
    notes_db[current_index] = note
    return "Note created!"


@router.put("/notes/{note_id}", status_code=status.HTTP_200_OK, tags=["notes"])
async def update_note(note_id: int, note: str = Body(...)):
    if note_id not in notes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    notes_db[note_id] = note
    return "Note updated!"


@router.delete("/notes/{note_id}", status_code=status.HTTP_200_OK, tags=["notes"])
async def delete_note(note_id) -> str:
    if note_id not in notes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    notes_db.pop(note_id)
    return f"Note ID={note_id} deleted!"


@router.delete("/notes", status_code=status.HTTP_200_OK, tags=["notes"])
async def delete_notes() -> str:
    notes_db.clear()
    return "All notes deleted!"
