from fastapi import FastAPI
from routes.drinks import drink

app = FastAPI()

app.include_router(drink)
