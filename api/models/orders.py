from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from datetime import datetime


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    #description = Column(String(255), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    tracking_number = Column(String(50), nullable=True, unique=True)
    order_status = Column(String(50), nullable=False, default="Pending")



    # Relationships
    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="order", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="order", cascade="all, delete-orphan")
    sandwich = relationship("Sandwich", back_populates="orders")