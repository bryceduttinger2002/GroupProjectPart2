from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model  # Fixed the import statement
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime


def create(db: Session, request):
    new_item = model.Order(
        customer_id=request.customer_id,
        sandwich_id=request.sandwich_id,
        quantity=request.quantity,# Ensure these fields exist in the request and model
        #description=request.description
        order_date=request.order_date or datetime.utcnow(),
        tracking_number=request.tracking_number,
        order_status=request.order_status or "Pending",
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, order_id):  # Changed item_id to order_id
    try:
        item = db.query(model.Order).filter(model.Order.id == order_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item



def update(db: Session, order_id, request):  # Changed item_id to order_id
    try:
        item = db.query(model.Order).filter(model.Order.id == order_id)  # Changed item_id to order_id
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, order_id):  # Changed item_id to order_id
    try:
        item = db.query(model.Order).filter(model.Order.id == order_id)  # Changed item_id to order_id
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

