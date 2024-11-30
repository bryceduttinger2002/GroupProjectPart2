from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas.orders import OrderCreate, OrderUpdate, Order
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(request: OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[Order])
def read_all_orders(db: Session = Depends(get_db)):
    return controller.read_all(db=db)

@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = controller.read_one(db=db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, request: OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, order_id=order_id, request=request)

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    controller.delete(db=db, order_id=order_id)
    return {"detail": "Order deleted successfully"}
