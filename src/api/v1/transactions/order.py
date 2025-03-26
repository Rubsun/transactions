from http.client import HTTPException

from fastapi import APIRouter

from src.db.models.model import Order
from src.schemas import OrderRequest
from src.transaction_example.order import place_order_transaction

router = APIRouter()


@router.post("/", response_model=OrderRequest)
async def place_order(order_request: OrderRequest):
    try:
        order_id = await place_order_transaction(order_request.customer_id, order_request.products)
        return {"order_id": order_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

