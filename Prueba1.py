#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:46:58 2022

@author: hsim12
"""

import random
import math
import matplotlib.pyplot as plt

individuos = [[0,1,0,1,1,1,0,1,0],
              [1,0,0,1,0,1,0,0,1],
              [0,0,1,0,1,0,1,0,1],
              [0,0,0,1,1,1,0,0,1],
              [1,1,0,0,1,0,1,0,1],
              [1,1,0,1,0,1,0,1,0],
              [0,0,0,1,1,0,1,1,0],
              [0,0,0,1,1,0,1,0,1],
              [0,1,1,0,1,0,1,0,1],
              [1,0,1,1,0,0,0,0,1],
              [0,0,1,0,1,0,1,0,1],
              [0,0,1,1,0,0,0,1,0],
              [0,0,1,1,1,1,0,0,1]]

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
    '''
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal
    '''
    binario_decimal(listaprueba)


def binario_decimal(listaprueba):
    for i in listaprueba:
        decimal.append(int(i,2))
    # print(decimal)
    Vcad(decimal)
    
    
def Vcad(decimal):
    for i in decimal:
        vcad = i 
        xmax = int(9)
        xmin = int(1)
        x = xmin + vcad * ( (xmax - xmin) / (2**9 -1))
        real.append(x)
        adap = ((8 * math.cos(x)) + (x)+(5* (x*x)))
        adaptado.append(adap) 
    ruleta(listaprueba,decimal,real,adaptado)

"""Esto no sirve de momento"""
# def impresiones(sumatoria):
#     i=0
#     for b,d, x, adap in zip(listaprueba, decimal, real, adaptado):
#         i+=1
#         print("Cromosoma ", i)
#         print(f"\nEl binario es: {b}")
#         print(f"El decimal es: {d}")
#         print("El real sería " + str(x))
#         print("El adaptado sería " + str(adap))
"""FIN"""

def ruleta(listaprueba,decimal,real,adaptado):
    sumatoriaAdapt= sum(adaptado)
    valoresRuleta = []
    for ada in adaptado:
        operacionRuleta = (ada*100) /sumatoriaAdapt
        valoresRuleta.append(operacionRuleta)
    # print(sumatoriaAdapt)
    listaOrdenada = list(zip(listaprueba,decimal,real,adaptado,valoresRuleta))
    # print(a)
    # print("El orden por ruleta serìa: ")
    listaOrdenada.sort(key=lambda x:x[4], reverse=True)
    # print(listaOrdenada)
    mutacion(listaOrdenada)

"""Cruce de un Punto"""
def CruceDeUnPunto(parent1,parent2,punto):
    p1,p2 = list(parent1),list(parent2) #Convertir string a entero
    for i in range(punto,len(p1)):
        p1[i],p2[i] = p2[i],p1[i]       #Información genetica
    p1,p2 = ''.join(p1),''.join(p2)     #Convertir lista a string
    return p1,p2

for index in range(int(input("Cuantos cruces haras: \n"))):
    print("\n\n" + "Cruce de un punto: ")
    parent1 = input("Ingresa el primer padre: ")     #Cromosomas de los padres
    parent2 = input("Ingresa el segundo padre: ")
    print("\n")
    
    print('Parent1:',parent1)
    print('Parent2:',parent2)
    print("\n")

    punto = 5  #Punto de Cruce en bits

    print('Punto de Cruce: ',punto)
    print("\n")

    hijo1,hijo2 = CruceDeUnPunto(parent1,parent2,punto)

    print('Hijo 1:',hijo1)     #Cromosomas de Hijo
    print('Hijo 2:',hijo2)
    print("\n\n")
    pass

"""FIN Cruce de un Punto"""

"""Cruce de Dos Puntos"""
def CruceDeDosPuntos(parent1,parent2,point,point2):
    p1,p2 = str(parent1),str(parent2) #Convertir string a entero
    hijo1 = ""
    hijo2 = ""
    longitud = len(parent1)
    while longitud > 0:
        for i in range(len(parent1)):
            print(longitud,i,p1[i], p2[i])
            if longitud <= point2 and longitud >= point:
                print("entre cruce:")
                hijo1 += p1[i]
                hijo2 += p2[i]
            else:
                print("fuera de cruce")
                hijo1 += p2[i]
                hijo2 += p1[i]
            
            longitud -= 1
        return hijo1,hijo2        
        
    
point = 3  #Punto de Cruce en bits
point2 = 5

for index in range(int(input("Cuantos cruces haras: \n"))):
    print("\n\n" + "Cruce de un punto: ")
    parent1 = str(input("Ingresa el primer padre: "))     #Cromosomas de los padres
    parent2 = str(input("Ingresa el segundo padre: "))
    print("\n")
    
    print('Padre 1:',parent1)
    print('Padre 2:',parent2)
    print("\n")

    print('Punto de Cruce: ',point)
    print("\n")

    hijo1,hijo2 = CruceDeDosPuntos(parent1,parent2,point,point2)

    print('Hijo 1:',hijo1)     #Cromosomas de Hijo
    print('Hijo 2:',hijo2)
    print("\n\n")
    pass
"""FIN Cruce de Dos Puntos"""

def mutacion(listaOrdenada):
    copiaArray = listaOrdenada.copy()
    listaOrdenada.clear()
    for i in range(len(copiaArray)):
        listaOrdenada += [list(copiaArray[i])]
    print(listaOrdenada)
    
    selectIndividuo = int(input("Que individuo se va a mutar: "))
    bitCambiar = int(input("Que bit se va a cambiar: "))
    mutarIndividuo = listaOrdenada[selectIndividuo-1]
    
    cadenaIndividuo = list(mutarIndividuo[0])
    
    if cadenaIndividuo[-bitCambiar] == '1':
        cadenaIndividuo[-bitCambiar] = '0'
    else:
        cadenaIndividuo[-bitCambiar] = '1'
        
    indivMutado = "".join(cadenaIndividuo)
    listaOrdenada[selectIndividuo-1][0] = indivMutado
    print("El individuo mutado es: ", listaOrdenada)
        
        






















binario_cadena(binario)
