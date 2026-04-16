from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.schemas.token import Token
from app.auth import hash_password, verify_password
from app.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["인증"])
