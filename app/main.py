from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, products, orders

app = FastAPI(
    title="Python API Demo",
    description="Eine einfache API für User, Product und Order Daten",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router registrieren
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/")
async def root():
    """Root-Endpunkt"""
    return {
        "message": "Python API Demo",
        "docs": "/docs",
        "endpoints": {
            "users": "/users",
            "products": "/products",
            "orders": "/orders"
        }
    }

