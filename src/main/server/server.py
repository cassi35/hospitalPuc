from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.responses import Response
from src.main.routes.endereco_routes import endereco_router
description = """ 
this is a api for hospital puc system.
"""
@asynccontextmanager
async def lifespan(app:FastAPI):
    print("server is initing...")
    yield
    print("server is shutting down...")
version = "v1"
app = FastAPI(title="hospital puc api", description=description, version=version,lifespan=lifespan)

@app.get('/')
async def root():
    return {"message": "Hospital PUC API is running"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)

app.include_router(endereco_router,prefix=f'/{version}/endereco',tags=["endereco"])