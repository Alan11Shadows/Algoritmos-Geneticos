#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:32:39 2022

@author: hsim17
"""

#PROGRAMA 3
#Solo el individuo 5

import random
import  math
import matplotlib.pyplot as plt

"""Convierte binarios a decimales"""

def binario_decimal(binario):
    numero_decimal = 0
    
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal


individuo5 = [1,0,1,0,1,1,0,1,0]

binario = individuo5

vcad = int(binario_decimal(binario))

xmin = int(1)
xmax = int(8)

x = xmin + vcad * ( (xmax - xmin) / (2**9 -1))

adaptado = (5 * (math.sin(x)) + (2 * (x **2)))



"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")



#decimal = 90
#real = 2.23
#adaptado = 13.92

sumatoria = 164.35

ruleta = (13.92 * 100) / sumatoria
print("La ruleta es: ")
print(ruleta)


# manzanas = [13.12,38.31,8.22,9.25,12]
# nombres = ["individuo 1", "individuo 2","individuo 3","individuo 4","individuo 5","individuo 6","individuo 7",]
# plt.pie(manzanas, labels=nombres)
# plt.show()