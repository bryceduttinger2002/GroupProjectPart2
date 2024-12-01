from sqlalchemy import Column, Integer, String, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    description = Column(String(300), nullable=True)
    order_date = Column(DATETIME, nullable=False, default=datetime.utcnow)
    total_price = Column(Float, nullable=True)

    # Relationships
    order_details = relationship("OrderDetail", back_populates="order")
    products = relationship("Product", secondary="order_product", back_populates="order")

    __table_args__ = {"extend_existing": True}
