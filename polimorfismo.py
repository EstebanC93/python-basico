# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:03:55 2021

@author: Esteban Henao
"""

class Persona():
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def Avanza(self):
        print("Hola soy "+self.nombre+" Ando Caminando")
              
class Ciclista(Persona):
    
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def Avanza(self):
        print("Hola soy "+self.nombre+" Ando moviendome en mi bicicleta")
        
def main():
    persona = Persona("David")
    persona.Avanza()
        
    ciclista = Ciclista("Daniel")
    ciclista.Avanza()
        
if __name__=='__main__':
    main()