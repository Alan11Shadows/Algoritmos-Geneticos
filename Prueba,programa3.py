#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:53:05 2022

@author: alan
"""
import math

individuos = ["0,1,0,1,0,0,1,0,1",
              "0,1,1,0,1,0,1,0,0",
              "0,0,1,1,0,1,0,0,1",
              "1,0,1,0,1,0,1,0,0",
              "0,0,0,1,1,0,0,1,0",
              "0,0,1,1,0,1,1,1,0",
              "0,0,1,1,1,0,1,0,1"]

"""Convirtiendo el binario a Decimal"""
binario = individuos

def binario_decimal(binario):
    numero_decimal = 0
    
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal

vcad = binario_decimal(individuos)

"""FIN"""

"""Resolviendo el real y el adaptado"""
for x in individuos:
    # xmax = int(15)
    # xmin = int(2)
    # x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
    # adaptado = (8 * (math.sin(x)) + (15 * (x)))
     
    # print("El binario ingresado es: " + str(binario) + "\n")
    # print("En decimal seria " + str(binario_decimal(binario)) + "\n")
    # print("El real sería " + str(x) + "\n")
    # print("El adaptado seria " + str(adaptado) + "\n" + "\n")

    print(x)
"""FIN"""



# individuos = [0,1,0,1,0,0,1,0,1],[0,1,1,0,1,0,1,0,0],[0,0,1,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0],[0,0,1,1,0,1,1,1,0],[0,0,1,1,1,0,1,0,1]


    
    
    











# mylist = [1,4,7,3,21]

# for x in mylist:
#   print(x)