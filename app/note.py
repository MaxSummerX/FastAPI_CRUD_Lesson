from fastapi import APIRouter, HTTPException, status


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
