from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.dependencies.database import Base, engine
from api.routers import (
    index_router,
    customers_router,
    orders_router,
    order_details_router,
    payments_router,
    promotions_router,
    reviews_router,
    recipes_router,
    resources_router,
    sandwiches_router,
)

# Lifespan context manager to handle database initialization
@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(debug=True, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index_router)
app.include_router(customers_router)
app.include_router(orders_router)
app.include_router(order_details_router)
app.include_router(payments_router)
app.include_router(promotions_router)
app.include_router(reviews_router)
app.include_router(recipes_router)
app.include_router(resources_router)
app.include_router(sandwiches_router)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Add a route for favicon.ico to suppress 404 logs
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {"message": "No favicon available"}
