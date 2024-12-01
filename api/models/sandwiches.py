from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    order_detail_id = Column(Integer, ForeignKey("order_details.id"), nullable=True)

    # Relationships
    order_detail = relationship("OrderDetail", back_populates="sandwiches")
    recipes = relationship("Recipe", back_populates="sandwich", cascade="all, delete-orphan")
