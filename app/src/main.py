from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from ..database import models
from ..database.database import engine
from .api import clientes, comodatos, recibos, users, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(clientes.router)
app.include_router(comodatos.router)
app.include_router(recibos.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"data": "Hola mundo"}
