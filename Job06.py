import pymysql

db = pymysql.connect(
    host = "localhost", 
    user = "root",
    password = "1234",
    database = "LaPlateforme"
    ) 

cursor = db.cursor()

sql = "SELECT SUM(capacite) as total FROM salles"
cursor.execute(sql)


result = cursor.fetchone()
print(f"La capacite des salles est de {result[0]}")

cursor.close()
db.close()