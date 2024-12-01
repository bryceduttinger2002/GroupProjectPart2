from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas.customers import CustomerCreate, CustomerUpdate, CustomerBase
from ..controllers import customers as controller

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerBase, status_code=status.HTTP_201_CREATED)
def create_customer(request: CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[CustomerBase])
def read_all_customers(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{customer_id}", response_model=CustomerBase)
def read_one_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, customer_id)

@router.put("/{customer_id}", response_model=CustomerBase)
def update_customer(customer_id: int, request: CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db, customer_id, request)

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, customer_id)
