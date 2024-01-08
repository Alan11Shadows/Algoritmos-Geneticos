#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 09:47:45 2022

@author: hsim25
"""
import random

"""Generando la longitud del ristra a travez del nùmero dado por el usuario"""
ingresa_ristra = input("Ingresa el tamaño de la ristra:  \n")
tamaño_ristra = int(ingresa_ristra)
print("El tamaño del ristra es de: " + ingresa_ristra + "\n")

"""Pedir el tamaño de la lista"""
ingresa_numero = input("Ingresa el tamaño de la lista:  \n")
tamaño_lista = int(ingresa_numero)
print("El tamaño de la lista es de: " + ingresa_numero + "\n")
    
"""Convirtiendo listas binarias a decimales"""
print("\nTus listas convertidas de binario a decimal: \n")
def binario_decimal(binario):
    numero_decimal = 0
    
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal

"""Generar el tamaño de la lista e imprimiendola"""
for i in range(tamaño_lista):
    binario =random.choices([0,1], k = tamaño_ristra)
    
    print(binario)
    print("En decimal seria " + str(binario_decimal(binario)) + "\n")
