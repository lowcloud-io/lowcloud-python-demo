from fastapi import APIRouter, HTTPException
from typing import List
from ..models.user import User
from ..services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()


@router.get("", response_model=List[User])
async def get_users():
    """Gibt alle Benutzer zurück"""
    return user_service.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Gibt einen Benutzer anhand der ID zurück"""
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user

