from .customers import Customer
from .model_loader import ModelLoader
from .order_details import OrderDetail
from .orders import Order
from .payments import Payment
from .promotions import Promotion
from .recipes import Recipe
from .resources import Resource
from .reviews import Review
from .sandwiches import Sandwich
from ..dependencies.database import Base, engine

# Define what should be accessible when importing `models`
__all__ = [
    "Customer",
    "ModelLoader",
    "OrderDetail",
    "Order",
    "Payment",
    "Promotion",
    "Recipe",
    "Resource",
    "Review",
    "Sandwich",
]

# Function to create all tables
def index():
    # Create all tables defined in the Base metadata
    Base.metadata.create_all(engine)
