from fastapi import APIRouter

from src.schemas import ProductCreate
from src.transaction_example.product import add_product_transaction

router = APIRouter()


@router.post("", response_model=ProductCreate)
async def add_product(product_data: ProductCreate):
    product = await add_product_transaction(product_data.product_name, product_data.price)
    return product