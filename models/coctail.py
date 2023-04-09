from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

coctails = Table("coctails", meta, Column(
    "id", Integer, primary_key=True), 
    Column("name", String(255)),
    Column("drink_type_id1", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("drink_type_id2", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("drink_type_id3", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("drink_type_id4", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("drink_type_id5", Integer, ForeignKey("drink_types.id"), nullable=False),
    Column("drink_type_id6", Integer, ForeignKey("drink_types.id"), nullable=False))