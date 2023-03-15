import pymysql

db = pymysql.connect(
    host = "localhost", 
    user = "root",
    password = "1234",
    database = "LaPlateforme"
    ) 

cursor = db.cursor()

sql = "SELECT SUM(superficie) as total FROM etage"
cursor.execute(sql)


result = cursor.fetchone()
print(f"La superficie de la Plateforme est de {result[0]}")

cursor.close()
db.close()