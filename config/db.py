from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Tartaglia3@localhost:3306/drinksdb")

meta = MetaData()

conn = engine.connect()