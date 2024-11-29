from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel
from api.schemas.order_details import OrderDetail

class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    total_price: float
    tracking_number: str
    status: Optional[str] = "pending"
    order_date: Optional[datetime] = datetime.now(timezone.utc)


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    total_price: Optional[float] = None
    tracking_number: Optional[str] = None
    status: Optional[str] = None
    order_date: Optional[datetime] = None

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    total_price: float
    tracking_number: str
    status: str

    class Config:
        orm_mode = True

