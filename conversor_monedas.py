# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
menu = input("""Menu
1. pesos colombianos
2. pesos argentinos
3. pesos mexicanos
Elije la moneda a la que desea convertir a dolares: 
""")

def moneda(nacionalidad,dolar):
    peso= int(input ("Ingrese la cantidad de pesos "+nacionalidad+": "))
    resultado = str(round(peso/dolar,2))
    peso=str(peso)
    print (peso + " pesos "+nacionalidad+ " equivale a: " + resultado + " dolares")
    
if menu == '1':
    moneda("Colombianos",3576)
    
elif menu == '2':
    moneda("Argentinos",91.21)
    
elif menu == '3':
    moneda("Mexicanos",20.67)
    
else:
    print("Opcion no valida")

