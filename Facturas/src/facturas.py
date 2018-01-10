# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a16manuelapg"
__date__ = "$Jan 10, 2018 11:28:46 AM$"

import os
os.environ['UBUNTU_MENUPROXY'] = '0'
import gi
import conexion
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class Factura:
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('Factura.glade')
        self.venprincipal = b.get_object('venprincipal')
        
        #Widgets de la ventana CLIENTES
        self.entdni = b.get_object('entdni')
        self.entnombre = b.get_object('entnombre')
        self.entapellidos = b.get_object('entapellidos')
        self.entdireccion = b.get_object('entdireccion')
        self.enttelefono = b.get_object('enttelefono')
        self.entlocalidad = b.get_object('entlocalidad')
        self.entemail = b.get_object('entemail')
        
        self.vistaclientes = b.get_object('vistaclientes')
        self.listaclientes = b.get_object('listaclientes')

        self.btnalta = b.get_object('btnalta')
        self.btnbaja = b.get_object('btnbaja')
        self.btnsalir = b.get_object('btnsalir')
                                
        #Widgets de la ventana COCHES

        dic = {'on_venprincipal_delete_event':self.salir,
        'on_btnalta_clicked':self.alta,'on_btnbaja_clicked':self.baja,'on_btnsalir_clicked':self.salir,}
        b.connect_signals(dic)
        self.venprincipal.show()
        conexion.listarclientes(self)

        
##Ahora vienen las funciones
    def iniciar(self,widget,data=None):
        var=1
    def alta(self,widget,data=None):
        if self.entdni.get_text() and self.entnombre.get_text() and self.entapellidos.get_text() and self.entdireccion.get_text() and self.enttelefono.get_text() and self.entlocalidad.get_text() and self.entemail.get_text() !="":
            
            self.dni = self.entdni.get_text()
            self.nombre = self.entnombre.get_text()
            self.apellidos = self.entapellidos.get_text()
            self.direccion = self.entdireccion.get_text()
            self.telefono = self.enttelefono.get_text()
            self.localidad = self.entlocalidad.get_text()
            self.email = self.entemail.get_text()
            
            self.fila = (self.dni, self.nombre, self.apellidos, self.direccion, self.telefono, self.localidad,self.email)
            conexion.insertar(self.fila)
            #modulos.limpiar(self)
            self.listaclientes.clear()
            conexion.listarclientes(self)
        
    def baja(self,widget,data=None):
        var=1
    def salir(self,widget,data=None):
        Gtk.main_quit()
       
if __name__ == '__main__':
    main = Factura()
    Gtk.main()
