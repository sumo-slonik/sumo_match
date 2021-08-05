from sqlalchemy import create_engine

DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                    server='localhost',
                                                                                    database='sumo_match_maker')
db = create_engine(DATABSE_URI)
print(db.table_names())
connection = db.connect()
print(connection.execute('select * from competitors').all())