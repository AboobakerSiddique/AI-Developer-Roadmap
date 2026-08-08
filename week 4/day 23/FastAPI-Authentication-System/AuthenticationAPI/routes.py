from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import User

from schemas import (
    UserCreate,
    UserLogin,
    UpdateUser
)

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

from logging_config import logger


router = APIRouter()


# ============================================================
# REGISTER
# ============================================================

@router.post("/register")
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Check username
    # --------------------------------------------------------

    existing_username = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if existing_username:

        logger.warning(
            "Registration failed - username already exists: %s",
            user_data.username
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # --------------------------------------------------------
    # Check email
    # --------------------------------------------------------

    existing_email = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_email:

        logger.warning(
            "Registration failed - email already exists: %s",
            user_data.email
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # --------------------------------------------------------
    # Hash password
    # --------------------------------------------------------

    hashed_password = hash_password(
        user_data.password
    )

    # --------------------------------------------------------
    # Create user
    # --------------------------------------------------------

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    logger.info(
        "User registered successfully: %s",
        new_user.username
    )

    return {
        "message": "User registered successfully"
    }


# ============================================================
# LOGIN
# ============================================================

@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Find user
    # --------------------------------------------------------

    user = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if not user:

        logger.warning(
            "Failed login attempt: %s",
            user_data.username
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    # --------------------------------------------------------
    # Verify password
    # --------------------------------------------------------

    password_correct = verify_password(
        user_data.password,
        user.hashed_password
    )

    if not password_correct:

        logger.warning(
            "Failed login attempt: %s",
            user_data.username
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    # --------------------------------------------------------
    # Create JWT
    #
    # IMPORTANT:
    # sub = username
    # This matches get_current_user()
    # --------------------------------------------------------

    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )

    logger.info(
        "User logged in successfully: %s",
        user.username
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ============================================================
# GET CURRENT USER
# ============================================================

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    logger.info(
        "Profile viewed: %s",
        current_user.username
    )

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }


# ============================================================
# UPDATE PROFILE
# ============================================================

@router.put("/profile")
def update_profile(
    user_data: UpdateUser,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Check username
    # --------------------------------------------------------

    existing_username = db.query(User).filter(
        User.username == user_data.username,
        User.id != current_user.id
    ).first()

    if existing_username:

        logger.warning(
            "Profile update failed - username already exists: %s",
            user_data.username
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # --------------------------------------------------------
    # Check email
    # --------------------------------------------------------

    existing_email = db.query(User).filter(
        User.email == user_data.email,
        User.id != current_user.id
    ).first()

    if existing_email:

        logger.warning(
            "Profile update failed - email already exists: %s",
            user_data.email
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # --------------------------------------------------------
    # Update user
    # --------------------------------------------------------

    current_user.username = user_data.username
    current_user.email = user_data.email

    db.commit()

    db.refresh(current_user)

    logger.info(
        "Profile updated successfully: %s",
        current_user.username
    )

    return {
        "message": "Profile updated successfully"
    }


# ============================================================
# DELETE ACCOUNT
# ============================================================

@router.delete("/account")
def delete_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    username = current_user.username

    logger.info(
        "Account deletion requested: %s",
        username
    )

    db.delete(current_user)

    db.commit()

    logger.info(
        "Account deleted successfully: %s",
        username
    )

    return {
        "message": "Account deleted successfully"
    }