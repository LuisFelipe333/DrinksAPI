from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

coctails = Table("coctails", meta, Column(
    "id", Integer, primary_key=True), 
    Column("name", String(255)))