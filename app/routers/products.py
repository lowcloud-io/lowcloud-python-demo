from fastapi import APIRouter, HTTPException
from typing import List
from ..models.product import Product
from ..services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])
product_service = ProductService()


@router.get("", response_model=List[Product])
async def get_products():
    """Gibt alle Produkte zurück"""
    return product_service.get_all_products()


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Gibt ein Produkt anhand der ID zurück"""
    product = product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return product

