# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "a16manuelapg"
__date__ = "$Oct 18, 2017 12:08:13 PM$"

from zipfile import ZipFile, BadZipfile
import re
def calcular(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = 'XYZ'
    reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
    return False
def limpiar(self):
    self.entdni.set_text("")
    self.entmodelo.set_text("")
    self.entnombre.set_text("")
    self.entmarca.set_text("")
    self.entmatricula.set_text("")
def limpiarcoche(self):
    self.entmatriculacoche.set_text("")
    self.entfecha.set_text("")
    self.entconcepto.set_text("")
    self.entprecio.set_text("")
    self.entunidades.set_text("")
def zipbackup(fichero):
    if fichero != "":
        try:
            with ZipFile(fichero + '.zip', 'w') as filezip:
                filezip.write(fichero)
                filezip.close()
        except BadZipfile:
            print "algun error al comprimier"
    else:
        print "no existe el fichero %s" % fichero
        
def restaurarzip(fichero):
    with ZipFile(fichero, 'r') as filezip:
        filezip.extractall('/home/a16manuelapg/NetBeansProjects/PROYECTO_A/src/copias_restauradas')
        filezip.close()

def calcularemail(email):
    if re.match("[^@]+@[^@]+\.[^@]+",email.lower()):
        return True
    else:
        return False