import pymysql

db = pymysql.connect(
    host = "localhost", 
    user = "root",
    password = "1234",
    database = "LaPlateforme"
    ) 

cursor = db.cursor()

sql = "SELECT salaire FROM employes"
cursor.execute(sql)


result = cursor.fetchall()

print(result)

cursor.close()
db.close()