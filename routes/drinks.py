from fastapi import APIRouter
from config.db import conn
from models.drink import drinks
from models.drinkType import drinkTypes

drink = APIRouter()

@drink.get("/drinks")
def get_drinks():
    return conn.execute(drinks.select()).fetchall

