import json
import os
from pathlib import Path
from typing import Dict, List, Any


class DataLoader:
    """Singleton-Klasse zum Laden und Cachen von JSON-Daten"""
    
    _instance = None
    _cache: Dict[str, List[Dict[str, Any]]] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance
    
    def _get_data_path(self, filename: str) -> Path:
        """Gibt den absoluten Pfad zur JSON-Datei zurück"""
        base_dir = Path(__file__).parent.parent.parent
        return base_dir / "data" / filename
    
    def load_data(self, filename: str) -> List[Dict[str, Any]]:
        """Lädt Daten aus einer JSON-Datei (mit Caching)"""
        if filename in self._cache:
            return self._cache[filename]
        
        file_path = self._get_data_path(filename)
        
        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self._cache[filename] = data
        return data
    
    def clear_cache(self):
        """Löscht den Cache (nützlich für Tests oder Neuladen)"""
        self._cache.clear()

