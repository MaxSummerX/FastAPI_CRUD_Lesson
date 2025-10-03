from fastapi import APIRouter, Body, HTTPException, status


router = APIRouter()

comments_db = {0: "First comment in FastAPI"}


@router.get("/comments", tags=["comments"])
async def read_comments() -> dict[int, str]:
    return comments_db


@router.get("/comments/{comment_id}", tags=["comments"])
async def read_comment(comment_id: int) -> str:
    try:
        return comments_db[comment_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


@router.post("/comments", status_code=status.HTTP_201_CREATED, tags=["comments"])
async def create_comment(comments: str = Body(...)) -> str:
    current_index = max(comments_db) + 1 if comments_db else 0
    comments_db[current_index] = comments
    return "Comment created!"


@router.put("/comments/{comment_id}", status_code=status.HTTP_200_OK, tags=["comments"])
async def update_comment(comment_id: int, comment: str = Body(...)) -> str:
    if comment_id not in comments_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    comments_db[comment_id] = comment
    return "Comment updated!"


@router.delete("/comments/{comment_id}", status_code=status.HTTP_200_OK, tags=["comments"])
async def delete_comment(comment_id: int) -> str:
    if comment_id not in comments_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    comments_db.pop(comment_id)
    return "Comment deleted!"


@router.delete("/comments", status_code=status.HTTP_200_OK, tags=["comments"])
async def delete_comments() -> str:
    comments_db.clear()
    return "All comments deleted!"
