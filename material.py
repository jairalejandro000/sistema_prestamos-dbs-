from pymongo import MongoClient
import requests as r
import pymysql as msqlc


class Material:
    def __init__(self):
        self.nombre = ""
        self.cantidad = 0
        self.descripcion = ""

    def __str__(self):
        if(len(self.lista)>0):
            return str(len(self.lista))+'registros'
        return self.nombre +" "+ self.cantidad +" "+self.descripcion
    
    def addMaterial(self, material):
        addMaterialmongoDB(self,material)
        #addMaterialMysql(self,material)
        return("Material agregado")
    
    def getMaterial(self):
        return(getMaterialmongoDB(self))
        #return(getMaterialMysql(self))


def addMaterialmongoDB(self, material):
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
            if "materiales" in self.collist:
                self.materiales = self.db["materiales"]
                self.nid = self.materiales.find().sort("_id",-1).limit(1)
                for x in self.nid:
                    f = int(x["_id"] +1)
                    self.materiales.insert_one({ "_id": f,"nombre": material.nombre, "cantidad": int(material.cantidad), "descripcion": material.descripcion })
            else:
                self.db = self.client["sistema-prestamos"]
                self.materiales = self.db["materiales"]
                self.materiales.insert_one({"_id": 1, "nombre": material.nombre, "cantidad": int(material.cantidad), "descripcion": material.descripcion })
        self.client.close()
    
def getMaterialmongoDB(self):
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
            self.materiales = self.db["materiales"]
            self.cant = self.materiales.find().count()
            if "materiales" in self.collist:
                nid = self.materiales.find()
                return(nid)
            elif self.cant == 0:
                return("No hay materiales disponibles")
        self.client.close()


def getMaterialMysql(self):
    try:
        self.mydb = msqlc.connect(host="localhost", user="root")
    except (msqlc.Error):
        print("Error en la conexion a la base de datos")
    else:
        self.get = self.mydb.cursor()
        self.get.execute("SELECT * FROM sistemaprestamos.materiales")
        self.cant = self.mydb.cursor()
        self.cant.execute("SELECT count(nombre) as cantidad FROM sistemaprestamos.materiales")
        for x in self.cant:
            if x[0] == 0:
                return("No hay materiales")
            else:
                return(self.get)
        self.mydb.close()

def addMaterialMysql(self, material):
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
            if "materiales" in xx[0]:
                self.insert = self.mydb.cursor()
                self.sql = "INSERT INTO materiales (nombre, cantidad, descripcion) VALUES (%s,%s,%s)"
                self.val = (material.nombre, int(material.cantidad), material.descripcion)
                self.insert.execute(self.sql, self.val)
            else:
                self.personas = self.mydb.cursor()
                self.personas.execute("CREATE TABLE materiales (_id INT AUTO_INCREMENT, nombre VARCHAR(255), cantidad INT(3), descripcion VARCHAR(255) PRIMARY KEY (_id))")
                self.insert = self.mydb.cursor()
                self.sql = "INSERT INTO materiales (nombre, cantidad, descripcion) VALUES (%s,%s,%s)"
                self.val = (material.nombre, int(material.cantidad), material.descripcion)
                self.insert.execute(self.sql, self.val)
        self.mydb.close()
    
