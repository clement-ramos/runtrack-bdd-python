import pymysql

db = pymysql.connect(
    host = "localhost", 
    user = "root",
    password = "1234",
    database = "LaPlateforme"
    ) 

cursor = db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM etudiants"

cursor.execute(sql)
print(cursor.fetchall())

cursor.close()
db.close()