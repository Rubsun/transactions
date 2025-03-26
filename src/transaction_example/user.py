from src.db.models.model import Customer
from src.db.storage.db import async_session
from src.schemas import CustomerResponse


async def update_customer_email_transaction(customer_id, new_email):
    async with async_session() as session:
        async with session.begin():
            customer = await session.get(Customer, customer_id)
            if not customer:
                raise ValueError("Customer not found")
            customer.email = new_email
            return CustomerResponse(**customer.__dict__)

