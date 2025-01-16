from pydantic import BaseModel

#Esto es un esquema de datos para FastAPI

class UserData(BaseModel):
    name: str
    password: str

class UserId(UserData):
    id: int