# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "a16manuelapg"
__date__ = "$Oct 18, 2017 12:08:13 PM$"

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
    self.entnombre.set_text("")
    self.entapellidos.set_text("")
    self.entdireccion.set_text("")
    self.entemail.set_text("")
    self.enttelefono.set_text("")
    self.entlocalidad.set_text("")
    
def limpiarpro(self):
    self.entproducto.set_text("")
    self.entprecio.set_text("")
    self.entstock.set_text("")

def calcularemail(email):
    if re.match("[^@]+@[^@]+\.[^@]+",email.lower()):
        return True
    else:
        return False