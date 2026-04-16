import os
import uuid
from fastapi import APIRouter, UploadFile, HTTPException

router = APIRouter(prefix="/upload", tags=["업로드"])

UPLOAD_DIR = "uploads"
ALLOWED_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"]
MAX_SIZE = 5 * 1024 * 1024  # 5MB

os.makedirs(UPLOAD_DIR, exist_ok=True)
