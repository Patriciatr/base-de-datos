# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:56:14 2020

@author: Patricia
"""

import cx_Oracle
from datetime import datetime

def insertRelacion(conexion):
    #sería ir haciendo if y else if para cada tipo de relación 
    #cursor = conexion.cursor(), dentro de cada if
    #cursor.close(), al final
    print("1. Insertar en la relación compran ")
    print("2. Insertar en la relación formada_por ")
    print("3. Insertar en la relación tratamiento ")
    opc = int(input("¿Qué desea hacer? "))
    if opc == 1:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        cursor.close()
    elif opc == 2:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        cursor.close()
    elif opc == 3:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        cursor.close()
    else:
        print("Error, opción no válida")

    
    
    
def insertTabla(conexion): 
    #sería ir haciendo if y else if para cada tipo de entidad
    #cursor = conexion.cursor(), dentro de cada if
    #cursor.close(), al final
    print("1. Insertar fármacos ")
    print("2. Insertar fabricantes ")
    print("3. Insertar compradores ")
    print("4. Insertar pedidos ")
    opc = int(input("¿Qué desea hacer? "))
    if opc==1:
        
        cursor = conexion.cursor()
        id=int(input("Introduce el id: "))
        precio=float(input("Introduce el precio: "))
        nombre=input("Introduce el nombre: ")
        existencias=input("¿Esta en stock, eliminado o disponible?: ")
        tipo=input("Introduce el tipo (hospitalario, farmaceutico o general): ")
        descrip=input("Introduce la descripción: ")
        fecha=datetime.strptime((input("Introduce el precio: "), '%d/%m/%y'))
        fabricante = int(input("Introduce el CIF del fabricante: "))                       
        inserto = "INSERT INTO Farmacos(id, precio, nombre, existencias, tipo, descripcion, fecha_caducidad, FABRICANTES_CIF) VALUES(" + id + precio + nombre + existencias + tipo + descrip + fecha + fabricante + ");"
        cursor.execute(inserto)
        cursor.close()
        
    elif opc ==2:
        cursor = conexion.cursor()
        cif=int(input("Introduce el CIF del fabricante: ")) 
        cp=int(input("Introduce el código postal: ")) 
        direccion=input("Introduce la dirección: ")
        ciudad=input("Introduce la ciudad: ")
        pais=input("Introduce la país: ")
        inserto= "INSERT INTO Fabricantes(CIF, CP, direccion, ciudad, pais) VALUES("+cif+cp+direccion+ciudad+pais+");"
        cursor.execute(inserto)
        cursor.close()
    elif opc==3:
        cursor = conexion.cursor()
        id=int(input("Introduce el id: "))
        nombre=input("Introduce el nombre: ")
        direccion=input("Introduce la dirección: ")
        inserto= "INSERT INTO Compradores(id, nombre, dirección) VALUES("+"id"+nombre+direccion+");"
        cursor.execute(inserto)
        cursor.close()
    elif opc==4:
        cursor = conexion.cursor()
        id=int(input("Introduce el id: "))
        importe=float(input("Introduce el importe: "))
        fecha=datetime.strptime((input("Introduce el precio: "), '%d/%m/%y'))
        inserto= "INSERT INTO pedidos (id, importe, fecha_envio) VALUES("+id+importe+fecha+");"
        cursor.execute(inserto)
        cursor.close()
    else:
        print("Error, opción no válida")
    
    
def consulta(conexion):
    #sería ir haciendo if y else if para cada tipo de consulta
    #cursor = conexion.cursor(), dentro de cada if
    #cursor.close(), al final
    print("1. Consulta de ")
    print("2. Consulta de ")
    print("3. Consulta de ")
    print("4. Consulta de ")
    opc = int(input("¿Qué desea hacer? "))
    if opc==1:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        #for resultdo in cursor:
        #    print(resultado)
        cursor.close()
    elif opc ==2:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        #for resultdo in cursor:
        #    print(resultado)
        cursor.close()
    elif opc==3:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        #for resultdo in cursor:
        #    print(resultado)
        cursor.close()
    elif opc==4:
        cursor = conexion.cursor()
        
        #cursor.execute(inserto)
        #for resultdo in cursor:
        #    print(resultado)
        cursor.close()
    else:
        print("Error, opción no válida")
    
    
    
dsnStr = cx_Oracle.makedsn("afrodita.lcc.uma.es", "1521", "bdsalud")
conexion = cx_Oracle.connect(user="U79073864w", password="79073864w",dsn=dsnStr)
print(conexion.version)

print("1. Insertar tupla en una entidad ")
print("2. Insertar tupla en una relación ")
print("3. Hacer una consulta ")
print("4. Salir ")

opc = int(input("¿Qué desea hacer? "))
while opc != 4:
    if opc==1:
        insertTabla(conexion)
    elif opc ==2:
        insertRelacion(conexion)
    elif opc==3:
        consulta(conexion)
    else:
        print("Error, opción no encontrada")
        
    print("1. Insertar tupla en una entidad ")
    print("2. Insertar tupla en una relación ")
    print("3. Hacer una consulta ")
    print("4. Salir ")
    opc = int(input("¿Qué desea hacer? "))

conexion.close()