from sqlalchemy import Column, Integer, String, DATETIME, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    total_price = Column(Numeric(10,2), nullable=False)
    tracking_number = Column(String(50), unique=True, nullable=False)
    status = Column(String(50), nullable=False)


    # Relationships
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
    reviews = relationship("Review", back_populates="order")  # Added relationship for reviews
