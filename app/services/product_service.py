from typing import List, Optional
from ..models.product import Product
from ..repositories.json_repository import JSONRepository


class ProductService:
    """Service für Product-Business-Logik"""
    
    def __init__(self):
        self.repository = JSONRepository("products.json")
    
    def get_all_products(self) -> List[Product]:
        """Gibt alle Produkte zurück"""
        data = self.repository.get_all()
        return [Product(**product) for product in data]
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Gibt ein Produkt anhand der ID zurück"""
        product_data = self.repository.get_by_id(product_id)
        if product_data:
            return Product(**product_data)
        return None

