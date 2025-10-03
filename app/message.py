from fastapi import APIRouter, Body, HTTPException, status


router = APIRouter()

messages_db = {0: "First post in FastAPI"}


@router.get("/messages", tags=["messages"])
async def read_messages() -> dict:
    return messages_db


@router.get("/messages/{message_id}", tags=["messages"])
async def read_message(message_id: int) -> str:
    try:
        return messages_db[message_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@router.post("/messages", status_code=status.HTTP_201_CREATED, tags=["messages"])
async def create_message(message: str = Body(...)) -> str:
    current_index = max(messages_db) + 1 if messages_db else 0
    messages_db[current_index] = message
    return "Message created!"


@router.put("/messages/{message_id}", status_code=status.HTTP_200_OK, tags=["messages"])
async def update_message(message_id: int, message: str = Body(...)) -> str:
    if message_id not in messages_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    messages_db[message_id] = message
    return "Message update!"


@router.delete("/messages/{message_id}", status_code=status.HTTP_200_OK, tags=["messages"])
async def delete_message(message_id: int) -> str:
    if message_id not in messages_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    messages_db.pop(message_id)
    return f"Message ID={message_id} deleted!"


@router.delete("/messages", status_code=status.HTTP_200_OK, tags=["messages"])
async def delete_messages() -> str:
    messages_db.clear()
    return "All messages deleted!"
