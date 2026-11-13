from typing import Generator

import jwt

from app.repository import users as users_repository
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.security import decode_access_token

security = HTTPBearer()

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security),
                     db: Session = Depends(get_db)) -> User:
    try:
        user_id = decode_access_token(credentials.credentials)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401,detail="Invalid or expired token")

    user = users_repository.get_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=401,detail="Unauthorized")

    return user
