from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud 
from database import engine, localSession
from schemas import UserData, UserId
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app = FastAPI()

#funcion para traer la bbdd
def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/") # es un decorador, utilizamos un metodo http. En este caso la ruta del endpoint es un #
async def hello_world():
    return {"message": "Hello, World!"}

#rutas para aceder a la bbdd 
@app.get('/api/users/', response_class=list[UserId])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)