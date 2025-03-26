from src.db.models.model import Order
from src.db.models.model import OrderItem
from src.db.models.model import Product
from src.db.storage.db import async_session


async def place_order_transaction(customer_id, products):
    async with async_session() as session:
        async with session.begin():
            new_order = Order(customer_id=customer_id)
            session.add(new_order)
            total_amount = 0
            for product_id, quantity in products.items():
                product = await session.get(Product, product_id)
                if not product:
                    raise ValueError("Product not found")
                subtotal = product.price * quantity
                total_amount += subtotal
                order_item = OrderItem(order_id=new_order.id, product_id=product_id, quantity=quantity, sub_total=subtotal)
                session.add(order_item)
            new_order.total_amount = total_amount
    return new_order.id