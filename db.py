import pymysql as msqlc


mydb = msqlc.connect(host="localhost", user="root", password ="")
db = mydb.cursor()
db.execute("use sistemaprestamos")
insertar = mydb.cursor()
sql = "INSERT INTO sistemaprestamos.personas (nombre, correo, edad, sexo) VALUES ('dfdsf', 'dsf', 19, 'M')"
insertar.execute(sql)
cant = mydb.cursor()
cant.execute("SELECT count(nombre) as cantidad FROM sistemaprestamos.personas")
for x in cant:
    print(x[0])

