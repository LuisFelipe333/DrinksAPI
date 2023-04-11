from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine
from models.drinkType import drinkTypes

drinks = Table("relation_ingredients", meta, Column(
    "id", Integer, primary_key=True),
    Column("drink_type_id", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("coctails_id", Integer, ForeignKey("coctails.id"), nullable=False),
    Column("quantity", Integer))