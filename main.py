from logging import shutdown
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import startup_db, shutdown_db
from routes.bandeira import router as bandeira_router
from routes.dispositivos import router as dispositivos_router
from routes.dependencia import router as dependencia_router
from routes.tipo_dispositivo import router as tipo_dispositivos_router
from routes.tipo_consumidor import router as tipo_router
from routes.unidade_consumidora import router as consumidor_router
app = FastAPI(title='CALCULADORA DE CONSUMO DE ENERGIA ÉLETRICA')


app.add_event_handler("startup", func= startup_db)
app.add_event_handler("shutdown", func= shutdown_db)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#restart no main para a criação da rota raiz -->  uvicorn main:app --reload (usa no terminal :3)

app.include_router(tipo_router)
app.include_router(consumidor_router)
app.include_router(tipo_dispositivos_router)
app.include_router(dependencia_router)
app.include_router(dispositivos_router)
app.include_router(bandeira_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


