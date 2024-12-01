from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=schema.Payment)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=order_id)

@router.put("/{order_id}", response_model=schema.Payment)
def update(order_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, order_id=order_id, request=request)

@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)

