from sqlalchemy.orm import Session 

from models import User 
from schemas import UserData
#funciones necesarias para poder efectuar acciones en nuestra bbdd

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name). first()

def create_user (db: Session, user: UserData):
    #se deberia encriptar la contraseña para una buena practica. 
    fake_password = user.password + '#fake'
    new_user = User(name=user.name, password=fake_password)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user