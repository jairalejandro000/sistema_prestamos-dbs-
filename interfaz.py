import persona as p
import sys 
import material as m
import time

def read():
    x = input()
    if x == "a" or x == "A": 
       print("Nombre:")
       nombre = input()
       print("Correo:")
       correo = input()
       print("Edad:")
       edad = input()
       print("Sexo:")
       sexo = input()
       persona = p.Persona()
       per = p.Persona()
       persona.nombre = nombre
       persona.edad = edad
       persona.correo = correo
       persona.sexo = sexo
       per.addPersona(persona)
       menu_usuario_reg()
    if x == "b" or x == "B": 
       menu_usuario_reg()
    if x == "c" or x == "C": 
       print("Adios")
       sys.exit()
    
def readd():
    x = input()
    if x == "a" or x == "A": 
       #objetosmongoDB()
       objetosMysql()
       time.sleep(5)
       menu_usuario_reg()
       print("Indice persona:")
       indicep = input()
       print("Indice material:")
       indicem = input()
       print("Cantidad:")
       cantidad = input()
       import prestamo as pr
       prestamo = pr.Prestamo()
       pres = pr.Prestamo()
       pres.nombre = indicep
       pres.material = indicem
       pres.cantidad = cantidad
       prestamo.addPrestamo(pres)
       menu_usuario_reg()
    if x == "b" or x == "B": 
       #personasmongoDB()
       personasMysql()
       time.sleep(5)
       menu_usuario_reg()
    if x == "c" or x == "C": 
       #objetosmongoDB()
       objetosMysql()
       time.sleep(5)
       menu_usuario_reg()
    if x =="d" or x == "D":
       import prestamo as pr
       prestamo = pr.Prestamo()
       prestamo.getPrestamos()
       print("Indice prestamo:")
       indice = input()
       prestamo.updatePrestamo(indice)
       menu_usuario_reg()
    if x == "e" or x == "E":
      #prestamosmongoDB()
      prestamosMysql()
      time.sleep(5)
      menu_usuario_reg()
    if x == "f" or x == "F": 
       print("Nombre:")
       nombre = input()
       print("Cantidad:")
       cantidad = input()
       print("Descripcion:")
       descripcion = input()
       material = m.Material()
       mat = m.Material()
       material.nombre = nombre
       material.cantidad = cantidad
       material.descripcion = descripcion
       mat.addMaterial(material)
       menu_usuario_reg()
    if x == "g" or x == "G": 
       print("Adios")
       sys.exit()

def menu():
    print("----------------Menú-----------------")
    print("Sistema de prestamos.................")
    print(".....................................")
    print("a) Registrarme.......................")
    print("b) Ya soy cliente....................")
    print("c) Salir.............................")
    print(".....................................")
    print(".....................................")
    read()

def menu_usuario_reg():
    print("----------------Menú-----------------")
    print(".....................................")
    print("Sistema de prestamos.................")
    print(".....................................")
    print("a) Hacer un prestamo.................")
    print("b) Ver personas......................")
    print("c) Ver material......................")
    print("d) Devolver..........................")
    print("e) Ver prestamos.....................")
    print("f) Agregar material..................")
    print("g) Salir.............................")
    print(".....................................")
    readd()

def prestamosmongoDB():
   print("----------Lista de prestamos---------")
   print(".....................................")
   print("Sistema de prestamos.................")
   print(".....................................")
   import prestamo as pr
   prestamos = pr.Prestamo()
   prestamos.getPrestamos()
   for x in prestamos.getPrestamos():
      print("Indice: ",x["_id"], x["persona"], x["material"], x["estado"])
   print(".....................................")
   print(".....................................")

def personasmongoDB():
    print("----------Lista de personas----------")
    print(".....................................")
    print("Sistema de prestamos.................")
    print(".....................................")
    persona = p.Persona()
    persona.getPersonas()
    for x in persona.getPersonas():
       print("Indice: ",x["_id"], x["nombre"], x["correo"], x["sexo"])
    print(".....................................")
    print(".....................................")

def objetosmongoDB():
   print("-----------Lista de objetos----------")
   print(".....................................")
   print("Sistema de prestamos.................")
   print(".....................................")
   material = m.Material()
   material.getMaterial()
   for x in material.getMaterial():
       print("Indice: ",x["_id"], x["nombre"],"Cantidad: ", x["cantidad"])
   print(".....................................")
   print(".....................................")

def personasMysql():
    print("----------Lista de personas----------")
    print(".....................................")
    print("Sistema de prestamos.................")
    print(".....................................")
    persona = p.Persona()
    persona.getPersonas()
    for x in persona.getPersonas():
       print("Indice: ",x[0], x[1], x[2], x[3])
    print(".....................................")
    print(".....................................")

def objetosMysql():
   print("-----------Lista de objetos----------")
   print(".....................................")
   print("Sistema de prestamos.................")
   print(".....................................")
   material = m.Material()
   material.getMaterial()
   for x in material.getMaterial():
       print("Indice: ",x[0], x[1], "Cantiadad: ", x[2], x[3])
   print(".....................................")
   print(".....................................")

def prestamosMysql():
   print("----------Lista de prestamos---------")
   print(".....................................")
   print("Sistema de prestamos.................")
   print(".....................................")
   import prestamo as pr
   prestamos = pr.Prestamo()
   prestamos.getPrestamos()
   for x in prestamos.getPrestamos():
      print("Indice: ",x[0], x[1], x[2], x[3])
   print(".....................................")
   print(".....................................")
menu()