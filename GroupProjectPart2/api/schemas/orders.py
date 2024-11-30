from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Base schema
class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None

# Schema for creating an order
class OrderCreate(OrderBase):
    pass

# Schema for updating an order
class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None

# Schema for the order response
class Order(OrderBase):
    id: int
    order_date: datetime
    total_price: Optional[float] = None  # Derived from `OrderDetail` if applicable
    order_details: List[dict] = []  # Replace `dict` with actual `OrderDetail` schema if needed

    class Config:
        orm_mode = True
