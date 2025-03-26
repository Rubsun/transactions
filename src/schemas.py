from pydantic import BaseModel


class OrderRequest(BaseModel):
    customer_id: str
    products: dict[str, int]

class EmailUpdate(BaseModel):
    new_email: str

class ProductCreate(BaseModel):
    product_name: str
    price: float

class ProductResponse(BaseModel):
    id: str
    product_name: str
    price: float

class CustomerResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str

class OrderResponse(BaseModel):
    order_id: str