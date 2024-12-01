from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail

class OrderBase(BaseModel):
    customer_id: int
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: List[OrderDetail] = None

    class ConfigDict:
        from_attributes = True