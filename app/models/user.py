from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    address: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Max Mustermann",
                "email": "max@example.com",
                "address": "Musterstraße 123, 12345 Musterstadt",
            }
        }
