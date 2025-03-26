from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.db.mixins.uuid_mixin import UUIDMixin
from src.db.models.meta import Base


class Customer(Base, UUIDMixin):
    __tablename__ = "customers"

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]

    orders: Mapped[list['Order']] = relationship('Order', back_populates='customer')



class Order(Base, UUIDMixin):
    __tablename__ = "orders"
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id", ondelete="CASCADE"))
    order_date: Mapped[datetime] = mapped_column(default=datetime.now(tz=timezone.utc))
    total_amount: Mapped[float]


    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
    order_items_list: Mapped[list['OrderItem']] = relationship('OrderItem', back_populates='order')


class OrderItem(Base, UUIDMixin):
    __tablename__ = "order_items"
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
    sub_total: Mapped[float]

    order: Mapped['Order'] = relationship("Order", back_populates="order_items_list")
    product: Mapped['Product'] = relationship("Product", backref="order_items")


class Product(Base, UUIDMixin):
    __tablename__ = "products"
    product_name: Mapped[str]
    price: Mapped[float]

