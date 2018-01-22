# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a16manuelapg"
__date__ = "$Jan 10, 2018 11:28:46 AM$"

import os
os.environ['UBUNTU_MENUPROXY'] = '0'
import gi
import conexion
import modulos
import time
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
                                
        #Widgets de la ventana FACTURACION
        self.lblfactura = b.get_object('lblfactura')
        self.lblprecio = b.get_object('lblprecio')
        self.entcliente = b.get_object('entcliente')
        self.vistafacturas = b.get_object('vistafacturas')
        self.listafacturas = b.get_object('listafacturas')
        
        self.btnventa = b.get_object('btnventa')
        self.btnnoventa = b.get_object('btnnoventa')
        self.cmbpro = b.get_object('cmbpro')
        self.listacombo = b.get_object('listacombo')
        self.entcantidad = b.get_object('entcantidad')
        
        
        #Widgets de la ventana PRODUCTOS
        self.entproducto = b.get_object('entproducto')
        self.entprecio = b.get_object('entprecio')
        self.entstock = b.get_object('entstock')

        self.vistaproductos = b.get_object('vistaproductos')
        self.listaproductos = b.get_object('listaproductos')
        
        self.btnaltap = b.get_object('btnaltap')
        self.btnbajap = b.get_object('btnbajap')
        
        
        

        dic = {'on_venprincipal_delete_event':self.salir,
        'on_btnalta_clicked':self.alta,'on_btnbaja_clicked':self.baja,'on_btnsalir_clicked':self.salir,
        'on_vistaclientes_cursor_changed': self.selectdato,
        
        'on_btnventa_clicked':self.venta,'on_cmbpro_changed':self.selectpre,
        
        'on_btnaltap_clicked':self.altaproducto,'on_vistaproductos_cursor_changed': self.selectpro,
        }
        b.connect_signals(dic)
        self.venprincipal.show()
        self.venprincipal.maximize()
        conexion.listarclientes(self)
        conexion.listarfacturas(self)
        conexion.listarproductos(self)
        self.cargarcmb(self)
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
            modulos.limpiar(self)
        
    def baja(self,widget,data=None):
        if self.entdni.get_text():
            conexion.baja(self.entdni.get_text())
            
        self.listaclientes.clear()
        conexion.listarclientes(self)
        modulos.limpiar(self)
            
    def salir(self,widget,data=None):
        Gtk.main_quit()
        
    def venta(self,widget,data=None):
        self.fecha = time.strftime('%d/%m/%y')
        self.clidni = self.entcliente.get_text()
        fila = (self.clidni,self.fecha)
        
        conexion.altafac(fila)
        self.listafacturas.clear()
        conexion.listarfacturas(self)
        modulos.limpiar(self)
        
        conexion.listarfac(self)#Esto nos da el numero de facturas
       
       
    def altaproducto(self,widget,data=None):
        self.producto = self.entproducto.get_text()
        self.precio = self.entprecio.get_text()
        self.stock = self.entstock.get_text()
        fila = (self.producto,self.precio,self.stock)
        
        conexion.insertarproducto(fila)
        modulos.limpiarpro(self)
        self.listaproductos.clear()
        conexion.listarproductos(self)
       
    def cargarcmb(self,widget,data=None):
        lista=conexion.cargarpro()
        for registro in lista:
            self.listacombo.append(registro)
     
       
       
       
     
       
       
    def selectdato(self, widget, data=None):
        model, iter = self.vistaclientes.get_selection().get_selected()
        if iter != None:
            sdni = model.get_value(iter, 0)
            snome = model.get_value(iter, 1)
            sapel = model.get_value(iter, 2)
            sdir = model.get_value(iter, 3)
            smail = model.get_value(iter, 4)
            stel = model.get_value(iter, 5)
            sloc = model.get_value(iter, 6)
            
            
            self.entdni.set_text(sdni)
            self.entnombre.set_text(snome)
            self.entapellidos.set_text(sapel)
            self.entdireccion.set_text(sdir)
            self.entemail.set_text(smail)
            self.enttelefono.set_text(stel)
            self.entlocalidad.set_text(sloc)
            
            self.entcliente.set_text(sdni)
            
            
    def selectpro(self, widget, data=None):
        
        model, iter = self.vistaproductos.get_selection().get_selected()
        if iter != None:
            snome = model.get_value(iter, 1)
            spre = model.get_value(iter, 2)
            sstock = model.get_value(iter, 3)
            
            self.entproducto.set_text(snome)
            self.entprecio.set_text(spre)
            self.entstock.set_text(sstock)
    def selectpre(self, widget, data=None):
        
        index = self.cmbpro.get_active()
        model = self.cmbpro.get_model()
        self.item = model[index][0]
        
        lista=conexion.listaprecio(self.item)        
        
        for registro in lista:
            self.lblprecio.set_text(registro)
            
if __name__ == '__main__':
    main = Factura()
    Gtk.main()
