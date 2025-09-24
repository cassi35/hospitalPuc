from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.responses import Response
from src.main.routes.endereco_routes import endereco_router
from src.main.routes.convenio_routes import convenio_router
from src.main.routes.consulta_routes import consulta_router
from src.main.routes.exame_routes import exame_router
from src.main.routes.especialidade_routes import especialidade_router
from src.main.routes.financeiro_routes import financeiro_routes
from src.main.routes.funcionario_routes import funcionario_router
from src.main.routes.iinternacao_routes import internacao_router
from src.main.routes.leito_routes import leito_router   
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
app.include_router(convenio_router,prefix=f'/{version}/convenio',tags=["convenio"])
app.include_router(consulta_router,prefix=f'/{version}/consulta',tags=["consulta"])
app.include_router(especialidade_router,prefix=f'/{version}/especialidade',tags=["especialidade"])
app.include_router(exame_router,prefix=f'/{version}/exame',tags=["exame"])
app.include_router(financeiro_routes,prefix=f'/{version}/financeiro',tags=["financeiro"])
app.include_router(funcionario_router,prefix=f'/{version}/funcionario',tags=["funcionario"])
app.include_router(internacao_router,prefix=f'/{version}/internacao',tags=["internacao"])
app.include_router(leito_router,prefix=f'/{version}/leito',tags=["leito"])