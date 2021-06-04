# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:47:10 2021

@author: Esteban Henao
"""

class Lavadora:
    
    def __init__(self):
        pass
    
    def lavar(self, temperatura = "caliente"):
        self.__llenar_tanque_de_agua(temperatura)
        self.__anhadir_jabon()
        self.__lavar()
        self.__centrifugar()
        
    def __llenar_tanque_de_agua(self,temperatura):
        print("Llenando el tanque con agua "+temperatura)
        
    def __anhadir_jabon(self):
        print("anhadiendo jabon")
        
    def __lavar(self):
        print("Lavando la ropa")
        
    def __centrifugar(self):
        print("Centrifugando la ropa")
        
if __name__=="__main__":
    lavadora = Lavadora()
    lavadora.lavar()