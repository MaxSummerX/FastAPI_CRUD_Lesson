from fastapi import APIRouter, HTTPException, status

from app.models.models import Message, MessageCreate


router = APIRouter()

messages_db: list[Message] = [Message(id=0, content="First post in FastAPI")]


# GET /messages: Возвращает весь список сообщений
@router.get("/messages", response_model=list[Message], tags=["messages"])
async def read_messages() -> list[Message]:
    return messages_db


# GET /messages/{message_id}: Получение одного сообщения по ID
@router.get("/messages/{message_id}", response_model=Message, tags=["messages"])
async def read_message(message_id: int) -> Message:
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


# POST /messages: Создание нового сообщения
@router.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED, tags=["messages"])
async def create_message(message_create: MessageCreate) -> Message:
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=message_create.content)
    messages_db.append(new_message)
    return new_message


# PUT /messages/{message_id}: Обновление существующего сообщения
@router.put("/messages/{message_id}", response_model=Message, status_code=status.HTTP_200_OK, tags=["messages"])
async def update_message(message_id: int, message_create: MessageCreate) -> Message:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            updated_message = Message(id=message_id, content=message_create.content)
            messages_db[i] = updated_message
            return updated_message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


# DELETE /messages/{message_id}: Удаление одного сообщения
@router.delete("/messages/{message_id}", status_code=status.HTTP_200_OK, tags=["messages"])
async def delete_message(message_id: int) -> dict:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            messages_db.pop(i)
            return {"detail": f"Message ID={message_id} deleted!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


# DELETE /messages: Удаление всех сообщений
@router.delete("/messages", status_code=status.HTTP_200_OK, tags=["messages"])
async def delete_messages() -> dict:
    messages_db.clear()
    return {"detail": "All messages deleted!"}
