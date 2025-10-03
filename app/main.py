from fastapi import FastAPI

from app.comment import router as comment_router
from app.message import router as message_router
from app.note import router as note_router


app = FastAPI(
    debug=True,  # Нужно для отладки приложения, в продакшене ставить False
    title="FastAPI Project",  # Название API
    summary="My CRUD application.",  # добавить краткое описание API
    description="The CRUD application supports **writing**, *reading*, updating, and deleting messages.",  # Подробного описания, поддерживающий синтаксис Markdown
    version="0.0.1",  # Версия приложения
    openapi_url="/api/v1/openapi.json",  # определяет URL, по которому доступна схема OpenAPI в формате JSON
    openapi_tags=[
        {"name": "messages", "description": "Messages operations"},
        {"name": "notes", "description": "Notes operations"},
        {"name": "comments", "description": "Comments operations"},
    ],  # Группировки операций в документации через tags
    docs_url="/swagger-docs",  # Путь к которому задаётся Swagger UI
    redoc_url=None,  # Путь к которому задаётся ReDoc. None - чтобы отключить
    swagger_ui_oauth2_redirect_url="/custom-oauth-redirect",  # Поддержки OAuth2 в Swagger UI
    swagger_ui_init_oauth={
        "clientId": "your-client-id"
    },  # Настройка параметры OAuth2 для кнопки "Authorize" в Swagger UI
)

app.include_router(message_router)
app.include_router(note_router)
app.include_router(comment_router)
