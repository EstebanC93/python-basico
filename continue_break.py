# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:01:34 2021

@author: Esteban Henao
"""

def run():
    '''for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)'''
    
    '''for i in range(10000):
        print(i)
        if i == 1054:
            break'''
            
    frase = input("Ingrese una frase corta: ")
    for letra in frase:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()