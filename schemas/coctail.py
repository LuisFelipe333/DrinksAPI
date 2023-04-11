from typing import Optional
from pydantic import BaseModel

class Coctail(BaseModel):
    id: Optional[int]
    name: str
