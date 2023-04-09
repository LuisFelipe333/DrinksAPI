from typing import Optional
from pydantic import BaseModel

class DrinkType(BaseModel):
    id: Optional[int]
    drink_type_name: str
    cont_alcohol: bool
    has_brands: bool