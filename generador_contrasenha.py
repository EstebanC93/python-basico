# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:42:44 2021

@author: Esteban Henao
"""
import random

def generar_contrasena():
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","T","S","U","V","W","X","Y","Z"]
    minuscula = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    simbolos = ["!","@","#","$","%","^","&","*","(",")","-","="]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    
    caracteres = mayusculas + minuscula + simbolos + numeros
    
    contrasenha = []
    
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasenha.append(caracter_random)
        
    contrasenha = "".join(contrasenha)
    return contrasenha


def run():
    contrasenha = generar_contrasena()
    print("Tu nueva contrasenha es" + contrasenha)

if __name__ == '__main__':
    run()