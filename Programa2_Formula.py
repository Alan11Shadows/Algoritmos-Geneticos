#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:52:14 2022

@author: hsim17
"""
#programa 2 Obtener la decodificacion (valor real del individuo)

import random
import  math
"""Convierte binarios a decimales"""

def binario_decimal(binario):
    numero_decimal = 0
    
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal
#binario = random.choices([0,1], k = 7)


x1 = [0,1,0,1,1,1,0]

individuo1 = [0,1,0,1,0,0,1,0,1]
individuo2 = [0,1,1,0,1,0,1,0,0]
individuo3 = [0,0,1,1,0,1,0,0,1]
individuo4 = [1,0,1,0,1,0,1,0,0]
individuo5 = [0,0,0,1,1,0,0,1,0]
individuo6 = [0,0,1,1,0,1,1,1,0]
individuo7 = [0,0,1,1,1,0,1,0,1]

binario = individuo1

"""Aplicando la formula """
#Formula f(x)= 8Senx + 15x

f2 = 37.27
f15 = 230.20

vcad = binario_decimal(binario)
# xmin = int(input("Ingresa el X minimo: "))
# xmax = int(input("Ingresa el X maximo: "))
xmax = int(15)
xmin = int(2)
x = xmin + vcad * ( (xmax - xmin) / (2**9 -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))


"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")


"""Individuo 2"""
binario = individuo2
vcad = int(binario_decimal(binario))
x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))
"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")

"""Individuo 3"""
binario = individuo3
vcad = int(binario_decimal(binario))
x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))
"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")

"""Individuo 4"""
binario = individuo4
vcad = int(binario_decimal(binario))
x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))
"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")

"""Individuo 5"""
binario = individuo5
vcad = int(binario_decimal(binario))
x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))
"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")

"""Individuo 6"""
binario = individuo6
vcad = int(binario_decimal(binario))
x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))
"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")

"""Individuo 7"""
binario = individuo7
vcad = int(binario_decimal(binario))
x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
adaptado = (8 * (math.sin(x)) + (15 * (x)))
"""Imprimiendo los resultados"""
print("El binario ingresado es: " + str(binario) + "\n")
print("En decimal seria " + str(binario_decimal(binario)) + "\n")
print("El real sería " + str(x) + "\n")
print("El adaptado seria " + str(adaptado) + "\n" + "\n")
