import uvicorn
from fastapi import FastAPI

from src.api.v1.transactions.order import router as order_router
from src.api.v1.transactions.product import router as product_router
from src.api.v1.transactions.user import router as user_router
app = FastAPI(title="Test Transaction API")

app.include_router(
    order_router,
    prefix="/orders",
    tags=["orders"]
)
app.include_router(
    product_router,
    prefix="/products",
    tags=["products"]
)
app.include_router(
    user_router,
    prefix="/users",
    tags=["users"]
)

