from typing import Optional
from pydantic import BaseModel

class RelationIngredient(BaseModel):
    id: Optional[int]
    drink_type_id: int
    coctail_id: int
    quantity: int