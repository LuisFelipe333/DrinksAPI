from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine
from models.drinkType import drinkTypes
from models.coctail import coctails
from models.relationIngredient import relationIngredients


drinks = Table("drinks", meta, Column(
    "id", Integer, primary_key=True),
    Column("drink_type_id", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("name", String(255)),
    Column("brand", String(255)),
    Column("app_price", Integer),
    Column("quantity", Integer))



meta.create_all(engine)
