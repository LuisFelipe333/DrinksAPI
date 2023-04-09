from sqlalchemy import Boolean, ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

drinkTypes = Table("drink_types", meta, Column(
    "id", Integer, primary_key=True),
    Column("drink_type_name", String(255)),
    Column("cont_alcohol", Boolean),
    Column("has_brands", Boolean))
