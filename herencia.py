# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:59:52 2021

@author: Esteban Henao
"""

class Rectangulo():
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
class Cuadrado(Rectangulo):
    
    def __init__(self,lado):    #inicializar sub clase
        super().__init__(lado, lado)   #inicializar super clase
        
if __name__=='__main__':
    rectangulo = Rectangulo(3, 4)
    print(rectangulo.area())
    
    cuadrado = Cuadrado(5)
    print(cuadrado.area())