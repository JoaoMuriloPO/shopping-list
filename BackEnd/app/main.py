from fastapi import FastAPI
from app.routes.routes import router as produto_router

app = FastAPI()

app.include_router(produto_router)