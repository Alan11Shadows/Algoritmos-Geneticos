#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:53:05 2022

@author: alan
"""
import math

individuos = [[0,1,0,1,0,0,1,0,1],
              [0,1,1,0,1,0,1,0,0],
              [0,0,1,1,0,1,0,0,1],
              [1,0,1,0,1,0,1,0,0],
              [0,0,0,1,1,0,0,1,0],
              [0,0,1,1,0,1,1,1,0],
              [0,0,1,1,1,0,1,0,1]]
listaprueba = []
decimal = []
listVcad = []
real = []
adaptado = []


"""Convirtiendo el binario a Decimal"""
binario = individuos

def binario_cadena(binario):
    
    for i in binario:
        binarioCadena = "".join([str(b) for b in i])
        listaprueba.append(binarioCadena)
    numero_decimal = 0
    '''
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal
    '''
    
def binario_decimal():
    for i in listaprueba:
        decimal.append(int(i,2))
    #print(decimal)

def Vcad():
    for i in decimal:
        vcad = i 
        xmax = int(15)
        xmin = int(2)
        x = (xmin + vcad) * ((xmax - xmin) / ((2 **9) -1))
        real.append(x)
        adap = (8 * (math.sin(x)) + (15 * (x)))
        adaptado.append(adap)

def impresiones():
    for b,d, x, adap in zip(listaprueba, decimal, real, adaptado):
        print(f"\nel binario es: {b}")
        print(f"el decimal es: {d}")
        #print("El binario ingresado es: " + str(binario) + "\n")
        #print("En decimal seria " + str(binario_decimal(binario)) + "\n")
        print("El real sería " + str(x))
        print("El adaptado seria " + str(adap) + "\n" + "\n")



binario_cadena(binario)
binario_decimal()
Vcad()
impresiones()


    


"""FIN"""

"""Resolviendo el real y el adaptado"""
#for x in individuos:
    # 
     
    # 

#    print(x)
"""FIN"""



# individuos = [0,1,0,1,0,0,1,0,1],[0,1,1,0,1,0,1,0,0],[0,0,1,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0],[0,0,1,1,0,1,1,1,0],[0,0,1,1,1,0,1,0,1]


    
    
    











# mylist = [1,4,7,3,21]

# for x in mylist:
#   print(x)