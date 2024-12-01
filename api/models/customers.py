from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(15), nullable=True)
    address = Column(String(255), nullable=False)

    # Relationships
    order_details = relationship("OrderDetail", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")  # Add this line