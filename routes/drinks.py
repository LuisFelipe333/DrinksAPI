from fastapi import APIRouter
from config.db import conn
from models.drink import drinks
from models.drinkType import drinkTypes
from schemas.drink import Drink

drink = APIRouter()

@drink.get("/drinks")
def get_drinks():
    return conn.execute(drinks.select()).fetchall
    
@drink.post("/drinks")
def create_drink(drink: Drink):
    new_drink = {"drink_type_id": drink.drink_type_id, "name": drink.name, "brand": drink.brand, "app_price": drink.app_price, "quantity": drink.quantity}
    result = conn.execute(drinks.insert().values(new_drink))
    return result 


