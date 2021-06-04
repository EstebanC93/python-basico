# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:29:07 2021

@author: Esteban Henao
"""
import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("elige un numero del 1 al 100: " ))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Elige un numero mas grande")
        else:
            print("Elige un numero mas pequenho")
        numero_elegido = int(input("Elige otro numero: "))
    print("acertaste!!!")

if __name__ == '__main__':
    run()