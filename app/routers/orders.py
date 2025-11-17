from fastapi import APIRouter, HTTPException
from typing import List
from ..models.order import Order
from ..services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])
order_service = OrderService()


@router.get("", response_model=List[Order])
async def get_orders():
    """Gibt alle Bestellungen zurück"""
    return order_service.get_all_orders()


@router.get("/{order_id}", response_model=Order)
async def get_order(order_id: int):
    """Gibt eine Bestellung anhand der ID zurück"""
    order = order_service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id {order_id} not found")
    return order

