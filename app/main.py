from fastapi import Body, FastAPI, HTTPException, status


app = FastAPI(
    debug=True,  # Нужно для отладки приложения, в продакшене ставить False
    title="FastAPI Project",  # Название API
    summary="My CRUD application.",  # добавить краткое описание API
    description="The CRUD application supports **writing**, *reading*, updating, and deleting messages.",  # Подробного описания, поддерживающий синтаксис Markdown
    version="0.0.1",  # Версия приложения
    openapi_url="/api/v1/openapi.json",  # определяет URL, по которому доступна схема OpenAPI в формате JSON
    openapi_tags=[
        {"name": "messages", "description": "Messages operations"}
    ],  # Группировки операций в документации через tags
    docs_url="/swagger-docs",  # Путь к которому задаётся Swagger UI
    redoc_url=None,  # Путь к которому задаётся ReDoc. None - чтобы отключить
    swagger_ui_oauth2_redirect_url="/custom-oauth-redirect",  # Поддержки OAuth2 в Swagger UI
    swagger_ui_init_oauth={
        "clientId": "your-client-id"
    },  # Настройка параметры OAuth2 для кнопки "Authorize" в Swagger UI
)

messages_db = {0: "First post in FastAPI"}


@app.get("/messages", tags=["messages"])
async def read_messages() -> dict:
    return messages_db


@app.get("/messages/{message_id}", tags=["messages"])
async def read_message(message_id: int) -> str:
    try:
        return messages_db[message_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@app.post("/messages", status_code=status.HTTP_201_CREATED, tags=["messages"])
async def create_message(message: str = Body(...)) -> str:
    current_index = max(messages_db) + 1 if messages_db else 0
    messages_db[current_index] = message
    return "Message created!"


@app.put("/messages/{message_id}", status_code=status.HTTP_200_OK, tags=["messages"])
async def update_message(message_id: int, message: str = Body(...)) -> str:
    if message_id not in messages_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    messages_db[message_id] = message
    return "Message update!"


@app.delete("/messages/{message_id}", tags=["messages"])
async def delete_message(message_id: int) -> str:
    pass


@app.delete("/messages", tags=["messages"])
async def delete_messages() -> str:
    pass
