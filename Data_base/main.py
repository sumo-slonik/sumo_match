import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin',
    database='sumo_match_maker'
)
print(db.is_connected())
myCursor = db.cursor()


data = ['Maciek', 'Nowakowski', 'Luks lubzina', '2', '2000-10-05', 'mężczyzna']
myCursor.execute('insert into competitors  VALUES (%s, %s, %s, %s, %s, %s)', data)
db.commit()
