from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from api.dependencies.database import Base  # Ensure this is the correct import path

class Customer(Base):
    __tablename__ = 'customers'  # Fixed typo here

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)




