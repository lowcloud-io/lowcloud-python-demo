from typing import List, Dict, Any, Optional
from .data_loader import DataLoader


class JSONRepository:
    """Generische Repository-Klasse für CRUD-Operationen auf JSON-Dateien"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.data_loader = DataLoader()
    
    def get_all(self) -> List[Dict[str, Any]]:
        """Gibt alle Einträge zurück"""
        return self.data_loader.load_data(self.filename)
    
    def get_by_id(self, item_id: int) -> Optional[Dict[str, Any]]:
        """Gibt einen Eintrag anhand der ID zurück"""
        items = self.get_all()
        for item in items:
            if item.get('id') == item_id:
                return item
        return None
    
    def find_by_field(self, field: str, value: Any) -> List[Dict[str, Any]]:
        """Findet Einträge anhand eines Feldes"""
        items = self.get_all()
        return [item for item in items if item.get(field) == value]

