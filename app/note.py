from fastapi import APIRouter


router = APIRouter()

notes_db = {0: "Study FastAPI", 1: "I like FastAPI"}


@router.get("/notes", tags=["notes"])
async def read_notes() -> dict:
    return notes_db
