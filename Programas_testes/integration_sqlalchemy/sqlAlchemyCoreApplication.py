from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table, ForeignKey, text

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData(schema='teste')
user = Table('user',
             metadata_obj,
             Column('pref_id', Integer, primary_key=True),
             Column('user_id', Integer,ForeignKey('user.pref_id'),nullable=False),
             Column('nome', String),
             Column('email', String(40)),
             Column('nickname', String(40)),
             Column('sexo', String(1)))



for table in metadata_obj.sorted_tables:
    print(table)

sql = text('select * from user')
result = engine.execute(sql)

for row in result:
    print(row)

sql_insert = text('insert into user values(1,"Gustavo","asd@gmail.com","gu","F")')
result = engine.execute(sql_insert)

for row in result:
    print(row)
