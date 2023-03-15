import pymysql

db = pymysql.connect(
    host = "localhost", 
    user = "root",
    password = "1234",
    database = "LaPlateforme"
    ) 

cursor = db.cursor()

sql = "SELECT nom, capacite FROM salles"
cursor.execute(sql)

for (nom, capacite) in cursor:
    print("Salle: {}, Capacité: {}".format(nom, capacite))

cursor.close()
db.close()