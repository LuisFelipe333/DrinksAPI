from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

drinkTypes = Table("drink_types", meta, Column(
    "id", Integer, primary_key=True),
    Column("drink_type_name", String(255))
    Column("cont_alcohol", Boolean)
    Column("cont_alcohol", Boolean))


drinks = Table("Drinks", meta, Column(
    "id", Integer, primary_key=True),
    Column("drink_type_id", Integer, ForeignKey("drinkTypes.id"), nullable=False),
    Column("name", String(255)),
    Column("brand", String(255)),
    Column("app_price", Integer))

coctails = Table("coctails", meta, Column(
    "id", Integer, primary_key=True), 
    Column("name", String(255)),
    Column("drink_type_id1", Integer, ForeignKey("drinkTypes.id"), nullable=False),
    Column("drink_type_id2", Integer, ForeignKey("drinkTypes.id"), nullable=False),
    Column("drink_type_id3", Integer, ForeignKey("drinkTypes.id"), nullable=False),
    Column("drink_type_id4", Integer, ForeignKey("drinkTypes.id"), nullable=False),
    Column("drink_type_id5", Integer, ForeignKey("drinkTypes.id"), nullable=False),
    Column("drink_type_id6", Integer, ForeignKey("drinkTypes.id"), nullable=False))

meta.create_all(engine)
