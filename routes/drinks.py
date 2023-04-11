from fastapi import APIRouter
from config.db import conn
from models.drink import drinks
from models.drinkType import drinkTypes
from schemas.drink import Drink
from schemas.drinkType import DrinkType
from sqlalchemy import select

drink = APIRouter()

@drink.get("/drinks")
def get_drinks():
    return conn.execute(drinks.select()).fetchall

@drink.get("/drinks/{id}")
def get_drink(id: int):    
    return conn.execute(drinks.select().where(drinks.c.id == id)).first()._mapping
    
@drink.post("/drinks")
def create_drink(drink: Drink):
    new_drink = {"drink_type_id": drink.drink_type_id, "name": drink.name, "brand": drink.brand, "app_price": drink.app_price, "quantity": drink.quantity}
    result = conn.execute(drinks.insert().values(new_drink))
    conn.commit()
    return conn.execute(drinks.select().where(drinks.c.id == result.lastrowid)).first()._mapping

@drink.get("/drink_types")
def get_drink_types():
    return conn.execute(drinkTypes.select()).fetchall

@drink.get("/drink_type/{id}")
def get_drink_type(id: int):
    return conn.execute(drinkTypes.select().where(drinkTypes.c.id == id)).first()._mapping

@drink.post("/drink_types")
def create_drink_type(drink_type: DrinkType):
    new_drink_type = {"drink_type_name": drink_type.drink_type_name, "cont_alcohol": drink_type.cont_alcohol, "has_brands": drink_type.has_brands}
    result = conn.execute(drinkTypes.insert().values(new_drink_type)) 
    conn.commit()
    return conn.execute(drinkTypes.select().where(drinkTypes.c.id == result.lastrowid)).first()._mapping
