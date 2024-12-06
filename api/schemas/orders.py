from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail

class OrderBase(BaseModel):
    customer_id: int
    #: Optional[str] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    #description: Optional[str] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: float

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: List[OrderDetail] = None

    class ConfigDict:
        from_attributes = True