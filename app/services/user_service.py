from typing import List, Optional
from ..models.user import User
from ..repositories.json_repository import JSONRepository


class UserService:
    """Service für User-Business-Logik"""
    
    def __init__(self):
        self.repository = JSONRepository("users.json")
    
    def get_all_users(self) -> List[User]:
        """Gibt alle Benutzer zurück"""
        data = self.repository.get_all()
        return [User(**user) for user in data]
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Gibt einen Benutzer anhand der ID zurück"""
        user_data = self.repository.get_by_id(user_id)
        if user_data:
            return User(**user_data)
        return None

