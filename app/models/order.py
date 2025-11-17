from pydantic import BaseModel
from datetime import datetime
from typing import List


class Order(BaseModel):
    id: int
    user_id: int
    product_ids: List[int]
    order_date: str
    total: float
    status: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "product_ids": [1, 2],
                "order_date": "2024-01-15T10:30:00",
                "total": 1499.98,
                "status": "completed"
            }
        }

