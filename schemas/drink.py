from typing import Optional
from pydantic import BaseModel

class Drink(BaseModel):
    id: Optional[int]
    drink_type_id: int
    name: str
    brand: str
    app_price: int