# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:43:54 2021

@author: Esteban Henao
"""

def palindromo(frase):
    frase = frase.replace(' ','')
    frase = frase.lower()
    frase_inv = frase[::-1]
    if frase == frase_inv:
        return True
    else:
        return False


def run():
    frase = input("Escribe una palabra: ")
    es_palindromo = palindromo(frase)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")


if __name__ == '__main__':
    run()