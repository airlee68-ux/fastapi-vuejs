from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.config import settings

from app.database import engine, Base
from app.models.post import Post  # noqa: F401
from app.models.user import User  # noqa: F401
from app.routers import post as post_router
from app.routers import upload as upload_router
from app.routers import auth as auth_router
from app.routers import ws as ws_router
from app.middleware import log_requests

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="게시판 API",
    description="FastAPI와 Vue.js로 만드는 게시판 서비스",
    version="0.1.0",
)

app.middleware("http")(log_requests)

origins = [
    origin.strip()
    for origin in settings.CORS_ORIGINS.split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(post_router.router)
app.include_router(upload_router.router)
app.include_router(ws_router.router)
