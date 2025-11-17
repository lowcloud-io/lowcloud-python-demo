from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Laptop",
                "description": "High-performance laptop",
                "price": 999.99,
                "category": "Electronics"
            }
        }

