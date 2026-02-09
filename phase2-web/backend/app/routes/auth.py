from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.db import get_session
from app.models import User
from app.schemas.auth import UserSignUp, UserSignIn, Token, UserResponse
from app.utils.auth import get_password_hash, verify_password, create_access_token

router = APIRouter()

@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
def signup(user_data: UserSignUp, session: Session = Depends(get_session)):
    statement = select(User).where(User.email == user_data.email)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        email=user_data.email,
        name=user_data.name,
        password_hash=get_password_hash(user_data.password)
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    access_token = create_access_token(data={"sub": new_user.id})
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user": UserResponse(id=new_user.id, email=new_user.email, name=new_user.name)
    }

@router.post("/signin", response_model=Token)
def signin(user_data: UserSignIn, session: Session = Depends(get_session)):
    statement = select(User).where(User.email == user_data.email)
    user = session.exec(statement).first()
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    access_token = create_access_token(data={"sub": user.id})
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user": UserResponse(id=user.id, email=user.email, name=user.name)
    }

@router.post("/signout")
def signout():
    return {"success": True}
