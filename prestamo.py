from interfaz import prestamos
from pymongo import MongoClient, database
from datetime import datetime 
import requests as r
import pymongo as msqlc


class Prestamo:
    def __init__ (self):
        self.nombre = ""
        self.material = ""
        self.cantidad = 0

    def addPrestamo(self, prestamo):
        #addPrestamomongoDB(self, prestamo)
        addPrestamoMysql(self, prestamo)
        return("Prestamo agregado")

    def updatePestamo(self, indice):
        #updatePrestamomongoDB(self, indice)
        updatePrestamoMysql(self, indice)

    def getPrestamos(self):
        #return(getPrestamosmongoDB())
        return(getPrestamosMysql())

def addPrestamomongoDB(self, prestamo):
    try:
        request = r.get("https://www.youtube.com/watch?v=3wcgbyHOfSs", timeout=10)
    except (r.ConnectionError, r.Timeout):
        print("Error en la conexion a la base de datos")
    else:
        print("Conexion a la base de datos exitosa")
        self.client = MongoClient("mongodb+srv://admin:12ab34cd@cluster.m4smi.mongodb.net/sistema-prestamos?retryWrites=true&w=majority")
        self.db = self.client["sistema-prestamos"]
        self.dblist = self.client.list_database_names()
        self.collist = self.db.list_collection_names()
        self.now = datetime.now()
        if "sistema-prestamos" in self.dblist:
            if "prestamos" in self.collist:
                self.prestamos = self.db["prestamos"]
                self.materiales = self.db["materiales"]
                self.personas = self.db["personas"]
                self.material = self.materiales.find({"_id":int(prestamo.material)})
                for x in self.material:
                    self.m = x["nombre"]
                    self.persona = self.personas.find({"_id":int(prestamo.nombre)})
                    for x in self.persona:
                        self.p = x["nombre"]
                        self.nid = self.prestamos.find().sort("_id",-1).limit(1)
                        for x in self.nid:
                            self.f = int(x["_id"] +1)
                            self.prestamos.insert_one({ "_id": self.f,"persona": self.p, "material": self.m, "cantidad": int(prestamo.cantidad), "estado": "Pendiente", "fecha_prestamo": self.now, "fecha_devolucion": "Pendiente" })
            else:
                self.materiales = self.db["materiales"]
                self.personas = self.db["personas"]
                self.material = self.materiales.find({"_id":int(prestamo.material)})
                for x in self.material:
                    m = x["nombre"]
                    self.persona = self.personas.find({"_id":int(prestamo.nombre)})
                    for x in self.persona:
                        p = x["nombre"]
                        self.prestamos = self.db["prestamos"]
                        self.prestamos.insert_one({ "_id": 1,"persona": p, "material": m, "cantidad": int(prestamo.cantidad), "estado": "Pendiente", "fecha_prestamo": self.now, "fecha_devolucion": "Pendiente" })
                        self.client.close() 

def getPrestamosmongoDB(self):
    try:
        request = r.get("https://www.youtube.com/watch?v=3wcgbyHOfSs", timeout=10)
    except (r.ConnectionError, r.Timeout):
        print("Error en la conexion a la base de datos")
    else:
        print("Conexion a la base de datos exitosa")
        self.client = MongoClient("mongodb+srv://admin:12ab34cd@cluster.m4smi.mongodb.net/sistema-prestamos?retryWrites=true&w=majority")
        self.db = self.client["sistema-prestamos"]
        self.dblist = self.client.list_database_names()
        self.collist = self.db.list_collection_names()
        if "sistema-prestamos" in self.dblist:
            self.prestamos = self.db["prestamos"]
            self.cant = self.prestamos.find().count()
            if "prestamos" in self.collist:
                nid = self.prestamos.find()
                return(nid)
            elif self.cant == 0:
                return("No hay prestamos")

def updatePrestamomongoDB(self, indice):
    try:
        request = r.get("https://www.youtube.com/watch?v=3wcgbyHOfSs", timeout=10)
    except (r.ConnectionError, r.Timeout):
        print("Error en la conexion a la base de datos")
    else:
        self.client = MongoClient("mongodb+srv://admin:12ab34cd@cluster.m4smi.mongodb.net/sistema-prestamos?retryWrites=true&w=majority")
        self.db = self.client["sistema-prestamos"]
        self.dblist = self.client.list_database_names()
        self.collist = self.db.list_collection_names()
        self.now = datetime.now()
        if "sistema-prestamos" in self.dblist:
            self.prestamos = self.db["prestamos"]
            self.cant = self.prestamos.find().count()
            if "prestamos" in self.collist:
                self.nid = { "_id": int(indice) }
                self.upp = { "$set": { "estado": "Completado", "fecha_devolucion": self.now } }
                self.prestamos.update_one(self.nid, self.upp)
            elif self.cant == 0:
                return("No hay prestamos")

def addPrestamoMysql(self, prestamo):
    try:
        self.mydb = msqlc.connect(host="localhost", user="root")
    except (msqlc.Error):
        print("Error en la conexion a la base de datos")
    else:
        print("Con conexión a internet")
        self.use = self.mydb.cursor()
        self.use.execute("USE sistemaprestamos")
        self.tb = self.mydb.cursor()
        self.tb.execute("SHOW TABLES")
        for xx in self.tb:
            if "prestamos" in xx[0]:
                self.insert = self.mydb.cursor()
                self.sql = "INSERT INTO prestamos (persona, material, cantidad, estado) VALUES (%s,%s,%s)"
                self.val = (prestamo.persona, prestamo.material, int(prestamo.cantidad), "Pendiente")
                self.insert.execute(self.sql, self.val)
            else:
                self.personas = self.mydb.cursor()
                self.personas.execute("CREATE TABLE prestamos (_id INT AUTO_INCREMENT, persona VARCHAR(255), material VARCHAR(255), cantidad INT(3), PRIMARY KEY (_id))")
                self.insert = self.mydb.cursor()
                self.sql = "INSERT INTO prestamos (persona, material, cantidad, estado) VALUES (%s,%s,%s)"
                self.val = (prestamo.persona, prestamo.material, int(prestamo.cantidad), "Pendiente")
                self.insert.execute(self.sql, self.val)

def updatePrestamoMysql(self, indice):
    try:
        self.mydb = msqlc.connect(host="localhost", user="root")
    except (msqlc.Error):
        print("Error en la conexion a la base de datos")
    else:
        self.use = self.mydb.cursor()
        self.use.execute("USE sistemaprestamos")
        self.tb = self.mydb.cursor()
        self.tb.execute("SHOW TABLES")
        for xx in self.tb:
            if "prestamos" in xx[0]:
                self.insert = self.mydb.cursor()
                self.sql = "UPDATE SET sistemaprestamos.prestamos.estado = Completado WHERE _id = %s"
                self.val = ("Completado")
                self.insert.execute(self.sql, self.val)
            else: 
                return("No hay prestamos")

def getPrestamosMysql(self):
    try:
        self.mydb = msqlc.connect(host="localhost", user="root")
    except (msqlc.Error):
        print("Error en la conexion a la base de datos")
    else:
        self.get = self.mydb.cursor()
        self.get.execute("SELECT * FROM sistemaprestamos.prestamos")
        self.cant = self.mydb.cursor()
        self.cant.execute("SELECT count(persona) as cantidad FROM sistemaprestamos.prestamos")
        for x in self.cant:
            if x[0] == 0:
                return("No hay prestamos")
            else:
                return(self.get)