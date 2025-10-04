from fastapi import APIRouter, HTTPException, status

from app.models.models import Message


router = APIRouter()

messages_db: list[Message] = [Message(id=0, content="First post in FastAPi")]


@router.get("/messages", response_model=list[Message], tags=["messages"])
async def read_messages() -> list[Message]:
    return messages_db


@router.get("/messages/{message_id}", response_model=Message, tags=["messages"])
async def read_message(message_id: int) -> Message:
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@router.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED, tags=["messages"])
async def create_message(message: Message) -> Message:
    if any(msg.id == message.id for msg in messages_db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The message ID already exists")
    messages_db.append(message)
    return message


@router.put("/messages/{message_id}", response_model=Message, status_code=status.HTTP_200_OK, tags=["messages"])
async def update_message(message_id: int, updated_message: Message) -> Message:
    if updated_message.id != message_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="The ID in the request body must match the ID in the path"
        )
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            messages_db[i] = updated_message
            return updated_message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@router.delete("/messages/{message_id}", status_code=status.HTTP_200_OK, tags=["messages"])
async def delete_message(message_id: int) -> dict:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            messages_db.pop(i)
            return {"detail": f"Message ID={message_id} deleted!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@router.delete("/messages", status_code=status.HTTP_200_OK, tags=["messages"])
async def delete_messages() -> dict:
    messages_db.clear()
    return {"detail": "All messages deleted!"}
