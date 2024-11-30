from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
