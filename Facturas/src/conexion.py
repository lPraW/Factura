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
        
def baja(self):
    try:
        cur.execute("delete from Cliente where dni = ?",(self.dato,))
        conex.commit()
    except sqlite3.Error:
        print("Hubo un error al borrar el cliente (este mensaje se ha lanzado desde el modulo conexion.py)")
        conex.rollback()