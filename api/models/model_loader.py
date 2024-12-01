from ..dependencies.database import Base, engine
from . import (
    orders,
    order_details,
    recipes,
    sandwiches,
    resources,
    customers,
    payments,
    promotions,
    reviews,
)

class ModelLoader:
    """
    A class responsible for managing the initialization and loading
    of database models into the database.
    """

    @staticmethod
    def create_tables():
        """
        Creates all tables in the database using SQLAlchemy's Base metadata.
        """
        print("Creating all tables in the database...")
        Base.metadata.create_all(engine)

    @staticmethod
    def drop_tables():
        """
        Drops all tables in the database.
        Use this with caution as it will remove all data!
        """
        print("Dropping all tables in the database...")
        Base.metadata.drop_all(engine)

    @staticmethod
    def load_models():
        """
        Additional logic for loading models or setting up relationships.
        """
        print("Loading models...")
        # Placeholder for any extra logic beyond table creation
