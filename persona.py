from mysql.connector.cursor import MySQLCursor
from pymongo import MongoClient
import requests as r
import pymysql as msqlc

class Persona:
    def __init__(self):
        self.nombre = ""
        self.correo = ""
        self.edad = 0
        self.sexo = ""

    def __str__(self):
        if(len(self.lista)>0):
            return str(len(self.lista))+'registros'
        return self.nombre +" "+ self.correo +" "+self.edad +" "+self.sexo
    
    def addPersona(self, persona):
        #addPersonamongoDB(self, persona)
        addPersonaMysql(self, persona)
        return("Persona registrada")

    def getPersonas(self):
        #return(getPersonasmongoDB(self))
        return(getPersonasMysql(self))
        

def addPersonamongoDB(self, persona):
    try:
        request = r.get("https://www.youtube.com/watch?v=3wcgbyHOfSs", timeout=10)
    except (r.ConnectionError, r.Timeout):
        print("Error en la conexion a la base de datos")
    else:
        self.client = MongoClient("mongodb+srv://admin:12ab34cd@cluster.m4smi.mongodb.net/sistemas-prestamos?retryWrites=true&w=majority")
        self.db = self.client["sistema-prestamos"]
        self.dblist = self.client.list_database_names()
        self.collist = self.db.list_collection_names()
        if "sistema-prestamos" in self.dblist:
            if "personas" in self.collist:
                self.personas = self.db["personas"]
                self.nid = self.personas.find().sort("_id",-1).limit(1)
                for x in self.nid:
                    self.f = int(x["_id"] +1)
                    self.personas.insert_one({ "_id": self.f,"nombre": persona.nombre, "correo": persona.correo, "edad": int(persona.edad), "sexo": persona.sexo })
            else:
                self.personas = self.db["personas"]
                self.personas.insert_one({"_id": 1, "nombre": persona.nombre, "correo": persona.correo, "edad": int(persona.edad), "sexo": persona.sexo })
        self.client.close()

def getPersonasmongoDB(self):
    try:
        request = r.get("https://www.youtube.com/watch?v=3wcgbyHOfSs", timeout=10)
    except (r.ConnectionError, r.Timeout):
        print("Error en la conexion a la base de datos")
    else:
        self.client = MongoClient("mongodb+srv://admin:12ab34cd@cluster.m4smi.mongodb.net/sistema-prestamos?retryWrites=true&w=majority")
        self.db = self.client["sistema-prestamos"]
        self.dblist = self.client.list_database_names()
        self.collist = self.db.list_collection_names()
        if "sistema-prestamos" in self.dblist:
            self.personas = self.db["personas"]
            self.cant = self.personas.find().count()
            if "personas" in self.collist:
                nid = self.personas.find()
                return(nid)
            elif self.cant == 0:
                return("No hay personas")
        self.client.close()


def addPersonaMysql(self, persona):
    try:
        self.mydb = msqlc.connect(host="localhost", user="root", passwd="", db="sistemaprestamos")
    except (msqlc.Error):
        print("Error en la conexion a la base de datos")
    else:
        self.use = self.mydb.cursor()
        self.use.execute("USE sistemaprestamos")
        self.tb = self.mydb.cursor()
        self.tb.execute("SHOW TABLES")
        for xx in self.tb:
            if "personas" in xx[0]:
                self.insert = self.mydb.cursor()
                self.sql = "INSERT INTO sistemaprestamos.personas (nombre, correo, edad, sexo) VALUES (%s,%s,%s,%s)"
                self.insert.execute(self.sql,(str(persona.nombre), str(persona.correo), int(persona.edad), str(persona.sexo)))
            else:
                self.personas = self.mydb.cursor()
                self.personas.execute("CREATE TABLE sistemaprestamos.personas (_id INT AUTO_INCREMENT, nombre VARCHAR(255), correo VARCHAR(255), edad INT(3), sexo CHAR(1), PRIMARY KEY (_id))")
                self.insert = self.mydb.cursor()
                self.sql = "INSERT INTO sistemaprestamos.personas (nombre, correo, edad, sexo) VALUES (%s,%s,%s,%s)"
                self.insert.execute(self.sql,(str(persona.nombre), str(persona.correo), int(persona.edad), str(persona.sexo)))
        self.mydb.close()
    
def getPersonasMysql(self):
    try:
        self.mydb = msqlc.connect(host="localhost", user="root")
    except (msqlc.Error):
        print("Error en la conexion a la base de datos")
    else:
        self.get = self.mydb.cursor()
        self.get.execute("SELECT * FROM sistemaprestamos.personas")
        self.cant = self.mydb.cursor()
        self.cant.execute("SELECT count(nombre) as cantidad FROM sistemaprestamos.personas")
        for x in self.cant:
            if x[0] == 0:
                return("No hay personas")
            else:
                return(self.get)
        self.mydb.close()