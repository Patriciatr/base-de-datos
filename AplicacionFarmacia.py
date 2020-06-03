# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:18:17 2020

@author: Patricia
"""
import cx_Oracle

def insertRelacion(conexion):
    print("1. Insertar en la relación compran ")
    print("2. Insertar en la relación formada_por ")
    print("3. Insertar en la relación tratamiento ")
    print("5. Salir")
    opc = int(input("¿Qué desea hacer? "))
    while opc !=5:
        if opc == 1:
            cursor = conexion.cursor()
            pedidos_id = input("Introduce el id del pedido: ")
            compradores_id = input("Introduce el id del comprador: ")
            inserto = "INSERT INTO compran (pedidos_id, compradores_id) VALUES(" + pedidos_id + ", " + compradores_id + ")"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
        elif opc == 2:
            cursor = conexion.cursor()
            farmacos_id = input("Introduce el id del farmaco: ")
            farmacos_cif = input("Introduce el CIF: ")
            pedidos_id = input("Introduce el id del pedido: ")
            cantidad = input("Introduce la cantidad: ")
            inserto = "INSERT INTO formada_por (farmacos_id, farmacos_cif, pedidos_id, cantidad) VALUES(" + farmacos_id + ", " + farmacos_cif + ", " + pedidos_id + ", "+ cantidad + ")"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
        elif opc == 3:
            cursor = conexion.cursor()
            farmacos_id = input("Introduce el id del farmaco: ")
            farmacos_fabricantes_cif = input("Introduce el CIF del fabricante: ")
            enfermedades_nombre = input("Introduce el nombre de la enfermedad: ")
            receta = input("Introduce la receta: ")
            inserto = "INSERT INTO tratamientos (farmacos_id, farmacos_fabricantes_cif, enfermedades_nombre, receta) VALUES(" + farmacos_id + ", " +  farmacos_fabricantes_cif + ", '" + enfermedades_nombre + "', '" + receta + "')"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
        else:
            print("Error, opción no válida")
        print("1. Insertar en la relación compran ")
        print("2. Insertar en la relación formada_por ")
        print("3. Insertar en la relación tratamiento ")
        print("5. Salir")
        opc = int(input("¿Qué desea hacer? "))
    
def insertTabla(conexion): 
    print("1. Insertar fármacos ")
    print("2. Insertar fabricantes ")
    print("3. Insertar compradores ")
    print("4. Insertar pedidos ")
    print("5. Salir")
    opc = int(input("¿Qué desea hacer? "))
    while opc !=5:
        if opc==1:
            
            cursor = conexion.cursor()
            id=input("Introduce el id: ")
            precio=input("Introduce el precio: ")
            nombre=input("Introduce el nombre: ")
            existencias=input("¿Esta en stock, eliminado o disponible?: ")
            tipo=input("Introduce el tipo (hospitalario, farmaceutico o general): ")
            descrip=input("Introduce la descripción: ")
            fecha=input("Introduce el fecha: ")
            fabricante = input("Introduce el CIF del fabricante: ")                     
            inserto = "INSERT INTO Farmacos(id, precio, nombre, existencias, tipo, descripcion, fecha_caducidad, FABRICANTES_CIF) VALUES(" + id+", " + precio+", '" + nombre+"', '" + existencias+"', '" + tipo+"', '" + descrip+"', TO_DATE('"+ fecha+"', 'dd-mm-yyyy'), " + fabricante + ")"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
            
        elif opc ==2:
            cursor = conexion.cursor()
            cif=input("Introduce el CIF del fabricante: ")
            cp=input("Introduce el código postal: ") 
            direccion=input("Introduce la dirección: ")
            ciudad=input("Introduce la ciudad: ")
            pais=input("Introduce la país: ")
            inserto= "INSERT INTO Fabricantes(CIF, CP, direccion, ciudad, pais) VALUES("+cif+", "+cp+", '"+direccion+"', '"+ciudad+"', '"+pais+"')"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
            
        elif opc==3:
            cursor = conexion.cursor()
            id=input("Introduce el id: ")
            nombre=input("Introduce el nombre: ")
            direccion=input("Introduce la dirección: ")
            inserto= "INSERT INTO Compradores(id, nombre, dirección) VALUES("+id+", '"+nombre+"', '"+direccion+"')"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
            
        elif opc==4:
            cursor = conexion.cursor()
            id=input("Introduce el id: ")
            importe=input("Introduce el importe: ")
            fecha=input("Introduce el fecha: ")
            inserto= "INSERT INTO pedidos (id, importe, fecha_envio) VALUES("+id+", "+importe+", TO_DATE('"+ fecha+"', 'dd-mm-yyyy')" +")"
            print(inserto)
            cursor.execute(inserto)
            cursor.close()
            
        else:
            print("Error, opción no válida")
            
        print("1. Insertar fármacos ")
        print("2. Insertar fabricantes ")
        print("3. Insertar compradores ")
        print("4. Insertar pedidos ")
        print("5. Salir")
        opc = int(input("¿Qué desea hacer? "))
    
def consulta1(conexion,CIF):
            cursor = conexion.cursor()
            consulta ="SELECT direccion, ciudad, pais FROM fabricantes WHERE CIF = "+CIF +""
            cursor.execute(consulta)
            for resultado in cursor:
                print(resultado)
            cursor.close()
def consulta2(conexion,nombre):
            cursor = conexion.cursor()
            consulta="SELECT compradores.nombre FROM compradores, compran, pedidos, formado_por, farmacos WHERE compradores.id = compran.compradores_id AND compran.pedidos_id = pedidos.id AND pedidos.id = formado_por.pedidos_id AND formado_por.farmacos_id = farmacos.id AND farmacos.nombre='"+nombre+"' "
            cursor.execute(consulta)
            for resultado in cursor:
                print(resultado)
            cursor.close()
def consulta3(conexion,pais):
            cursor = conexion.cursor()
            consulta="SELECT * FROM fabricantes WHERE pais='"+pais+"' ORDER BY CIF"
            cursor.execute(consulta)
            for resultado in cursor:
                print(resultado)
            cursor.close()
def consulta4(conexion,id):
            cursor = conexion.cursor()
            consulta="SELECT * FROM farmacos WHERE id = '"+ id +"'"
            cursor.execute(consulta)
            for resultado in cursor:
                print(resultado)
            cursor.close()
            
def consulta(conexion):
    print("1. Mostrar la dirección de un fabricante")
    print("2. Mostrar la lista de compradores que han comprado un fármaco específico")
    print("3. Mostrar todos los fabricantes de un pais")
    print("4. Mostrar los datos de un fármaco")
    print("5.Salir")
    opc = int(input("¿Qué desea hacer? "))
    while opc !=5:
        if opc==1:
            cif = input("Introduzca el CIF: ")
            consulta1(conexion,cif)
        elif opc==2:
            nombre=input("Introduzca el nombre del fármaco: ")
            consulta2(conexion,nombre)
        elif opc ==3:
            pais = input("Introduzca el pais:")
            consulta3(conexion,pais)
        elif opc==4:
            id = input("Introduzca el id: ")
            consulta4(conexion,id)
        else:
            print("Error, opción no válida")
            
        print("1. Mostrar la dirección de un fabricante")
        print("2. Mostrar la lista de compradores que han comprado un fármaco específico")
        print("3. Mostrar todos los fabricantes de un pais")
        print("4. Mostrar los datos de un fármaco")
        print("5.Salir")
        opc = int(input("¿Qué desea hacer? "))
    
dsnStr = cx_Oracle.makedsn("afrodita.lcc.uma.es", "1521", "bdsalud")
conexion = cx_Oracle.connect(user="U79073864w", password="79073864w",dsn=dsnStr, encoding = "UTF-8", nencoding = "UTF-8")
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

