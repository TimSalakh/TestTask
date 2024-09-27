from fastapi import FastAPI
from app.data.database import engine, Base
from app.routes import cart_routes, item_routes, user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router, prefix="/api/user")
app.include_router(item_routes.router, prefix="/api/item")
app.include_router(cart_routes.router, prefix="/api/cart")
