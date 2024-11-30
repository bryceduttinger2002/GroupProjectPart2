from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.orders import Order
from ..schemas.orders import OrderCreate, OrderUpdate
from fastapi import HTTPException, status

def create(db: Session, request: OrderCreate):
    new_order = Order(
        customer_name=request.customer_name,
        description=request.description
    )
    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return new_order

def read_all(db: Session):
    return db.query(Order).all()

def read_one(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update(db: Session, order_id: int, request: OrderUpdate):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(order, key, value)
    try:
        db.commit()
        db.refresh(order)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return order

def delete(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    try:
        db.delete(order)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
