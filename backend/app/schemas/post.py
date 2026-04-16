from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class PostCreate(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI 시작하기",
                "content": "FastAPI로 첫 번째 API를 만들어봅니다.",
                "image_url": None,
            }
        }
    )

    title: str = Field(
        min_length=2, max_length=100,
        description="게시글 제목",
    )
    content: str = Field(
        min_length=1, description="게시글 내용"
    )
    image_url: str | None = Field(
        None, max_length=500,
        description="이미지 URL",
    )


class PostResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "FastAPI 시작하기",
                "content": "FastAPI로 첫 번째 API를 만들어봅니다.",
                "image_url": None,
                "created_at": "2026-01-15T09:30:00",
            }
        },
    )

    id: int
    title: str
    content: str
    image_url: str | None
    created_at: datetime
