from typing import List, Optional
from ..models.order import Order
from ..repositories.json_repository import JSONRepository


class OrderService:
    """Service für Order-Business-Logik"""
    
    def __init__(self):
        self.order_repository = JSONRepository("orders.json")
        self.user_repository = JSONRepository("users.json")
        self.product_repository = JSONRepository("products.json")
    
    def get_all_orders(self) -> List[Order]:
        """Gibt alle Bestellungen zurück"""
        data = self.order_repository.get_all()
        return [Order(**order) for order in data]
    
    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        """Gibt eine Bestellung anhand der ID zurück"""
        order_data = self.order_repository.get_by_id(order_id)
        if order_data:
            return Order(**order_data)
        return None
    
    def validate_order_references(self, order: Order) -> bool:
        """Validiert, ob User und Products existieren"""
        user = self.user_repository.get_by_id(order.user_id)
        if not user:
            return False
        
        for product_id in order.product_ids:
            product = self.product_repository.get_by_id(product_id)
            if not product:
                return False
        
        return True

