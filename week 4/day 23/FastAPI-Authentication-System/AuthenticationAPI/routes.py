from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate
from auth import hash_password
from fastapi.security import OAuth2PasswordRequestForm
from auth import verify_token
from auth import get_current_user
from schemas import UpdateUser

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check username
    existing_username = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check email
    existing_email = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Hash password
    hashed = hash_password(user.password)

    # Create user
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }
    
@router.get("/profile")
def profile(
    current_user: str = Depends(verify_token)
):

    return {
        "message": "Protected Route",
        "username": current_user
    }
    
@router.get("/me")
def get_me(

    current_user = Depends(get_current_user)

):
    return {

    "id": current_user.id,

    "username": current_user.username,

    "email": current_user.email

}
    
@router.put("/profile")
def update_profile(
    user_data: UpdateUser,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user_data.username,
        User.id != current_user.id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    existing_email = db.query(User).filter(
        User.email == user_data.email,
        User.id != current_user.id
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    current_user.username = user_data.username
    current_user.email = user_data.email

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Profile updated successfully"
    }
    
@router.delete("/account")
def delete_account(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    db.delete(current_user)

    db.commit()

    return {
        "message": "Account deleted successfully"
    }