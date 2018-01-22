# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

 #!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "a16manuelapg"
__date__ = "$Oct 23, 2017 1:24:38 PM$"


import sqlite3

try:
 
    bbdd = 'factura.sqlite'
    conex = sqlite3.connect(bbdd)
    conex.text_factory = str

    cur = conex.cursor()
    
except:
    print('Error en la conexion de SQLITE (este mensaje se ha lanzado desde el modulo de conexion.py)')
    
    ##Funciones de CLIENTES
def insertar(fila):
    try:
        registro = fila
        cur.execute("insert into Cliente (dni,nombre,apellido,direccion,telefono,localidad,email) values (?,?,?,?,?,?,?)",registro)
        conex.commit()
    except sqlite3.Error:
        print("Hubo un error al insertar el cliente (este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()

def listacliente():
    try:
        cur.execute("select * from Cliente")
        listado = cur.fetchall()
        conex.commit()
        return listado
    except sqlite3.Error:
        print("Hubo un error al listar los clientes(este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
def listarclientes(self):
    lista=listacliente()
    for registro in lista:
        self.listaclientes.append(registro)
        
def baja(dni):
    try:
        cur.execute("delete from Cliente where dni = ?",(dni,))
        conex.commit()
    except sqlite3.Error:
        print("Hubo un error al borrar el cliente (este mensaje se ha lanzado desde el modulo conexion.py)")
        conex.rollback()
        
        
        
     ##Funciones de FACTURAS
     
def altafac(fila):
    try:
        registro = fila
        cur.execute("insert into Factura (id_cliente,fecha) values (?,?)",registro)
        conex.commit()
    except sqlite3.Error:
        print("Hubo un error al insertar la factura (este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
        
        
def listafactura():
    try:
        cur.execute("select * from Factura")
        listado = cur.fetchall()
        conex.commit()
        return listado
    except sqlite3.Error:
        print("Hubo un error al listar las facturas (este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
        
def listarfacturas(self):
    lista=listafactura()
    for registro in lista:
        self.listafacturas.append(registro)
def listarfac(self):
    try:
        cur.execute("select num_factura from Factura")
        listado = cur.fetchone()
        self.lblfactura.set_text(listado)
        conex.commit()
    except sqlite3.Error:
        print("Hubo un error al listar las facturas (este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
        
        
        
        
def insertarproducto(fila):
    try:
        registro = fila
        cur.execute("insert into Producto (nombre,precio,stock) values (?,?,?)",registro)
        conex.commit()
    except sqlite3.Error:
        print("Hubo un error al insertar el producto (este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
        
def listaproducto():
    try:
        cur.execute("select * from Producto")
        listado = cur.fetchall()
        conex.commit()
        return listado
    except sqlite3.Error:
        print("Hubo un error al listar los productos(este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
def listarproductos(self):
    lista=listaproducto()
    for registro in lista:
        self.listaproductos.append(registro)
        
def cargarpro():
    try:
        cur.execute("select nombre from Producto")
        listado = cur.fetchall()
        conex.commit()
        return listado
    except sqlite3.Error:
        print("Hubo un error al cargar el combo(este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()
        
        
def listaprecio(producto):
    try:
        cur.execute("select precio from Producto where nombre = ?", (producto,))
        listado = cur.fetchone()
        conex.commit()
        return listado
    except sqlite3.Error:
        print("Hubo un error al cargar el combo(este mensaje se ha lanzado desde el modulo de conexion.py)")
        conex.rollback()