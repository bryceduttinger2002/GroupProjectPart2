from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import customers as model
from ..schemas.customers import CustomerUpdate
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_customer = model.Customer(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address
    )
    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', 'Unknown error'))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_customer


def read_all(db: Session):
    try:
        result = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', 'Unknown error'))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, customer_id: int):
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', 'Unknown error'))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customer


def update(db: Session, customer_id: int, request: CustomerUpdate):
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")

        if request.name is not None:
            customer.name = request.name
        if request.email is not None:
            customer.email = request.email
        if request.phone is not None:
            customer.phone = request.phone
        if request.address is not None:
            customer.address = request.address

        db.commit()
        db.refresh(customer)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', 'Unknown error'))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return customer


def delete(db: Session, customer_id: int):
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
        db.delete(customer)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', 'Unknown error'))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
