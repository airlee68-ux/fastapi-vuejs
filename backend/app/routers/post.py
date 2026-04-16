from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload

from app.database import get_db
from app.deps import get_current_user
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["게시글"])


@router.get("/", summary="게시글 목록")
def list_posts(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
):
    offset = (page - 1) * size
    total = db.query(Post).count()
    posts = (
        db.query(Post)
        .options(selectinload(Post.author))
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(size)
        .all()
    )
    return {"items": posts, "total": total}
