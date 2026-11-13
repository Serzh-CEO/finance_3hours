from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependency import get_db
from app.repository import users as users_repository
from app.schemas import LoginRequest, TokenResponse
from app.security import verify_password, create_access_token

router = APIRouter(prefix="/auth")

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest,db:Session = Depends(get_db)):
    user = users_repository.get_user(db,payload.login)
    if not user or not verify_password(payload.password,user.hashed_password):
        raise HTTPException(status_code=401,detail="Invalid login or password")
    return TokenResponse(access_token=create_access_token(user.id))