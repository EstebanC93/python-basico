# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:44:08 2021

@author: Esteban Henao
"""

'''contador = 1
print(contador)
while contador < 1000:
    contador = contador + 1
    print(contador)'''

#for contador in range(1000):
    #print(contador)
    
    
#for i in range(10):
    #print(11 * i)
    
def run():
    nombre = input("ingrese su nombre: ")
    for letra in nombre:
        #print(letra)
        print(letra.upper())

if __name__ == '__main__':
    run()