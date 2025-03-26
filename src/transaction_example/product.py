from src.db.models.model import Product
from src.db.storage.db import async_session
from src.schemas import ProductResponse


async def add_product_transaction(product_name, price):
    async with async_session() as session:
        async with session.begin():
            new_product = Product(product_name=product_name, price=price)
            session.add(new_product)
            await session.flush()
            return ProductResponse(**new_product.__dict__)