from http.client import HTTPException

from fastapi import APIRouter, Form

from src.schemas import EmailUpdate
from src.transaction_example.user import update_customer_email_transaction

router = APIRouter()


@router.put("/{customer_id}/email")
async def update_customer_email(customer_id: str, email: EmailUpdate = Form(...)):
    try:
        updated_customer = await update_customer_email_transaction(customer_id, email.new_email)
        return updated_customer
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))