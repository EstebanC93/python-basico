# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:04:31 2021

@author: Esteban Henao
"""

#contador = 0
#print("2 elevado a "+ str(contador)+ "es igual a: " + str(2**contador))

def run():
    LIMITE = 1000
    
    contador = 0
    potencia_2=2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a "+ str(contador)+ "es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
        


if __name__ == "__main__":
    run()
