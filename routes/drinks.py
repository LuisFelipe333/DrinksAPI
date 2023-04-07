from fastapi import APIRouter

drink = APIRouter()

@drink.get("/drinks")
def helloworld():
    return "drinks"

