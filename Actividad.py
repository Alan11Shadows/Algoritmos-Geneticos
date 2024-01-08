#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:41:00 2022

@author: alan
"""

"""Adaptado, Real y Decimal"""
import math
import matplotlib.pyplot as plt

#GENERACION 1
# individuos = [[0,1,0,1,1,1,0,1,0],
#               [1,0,0,1,0,1,0,0,1],
#               [0,0,1,0,1,0,1,0,1],
#               [0,0,0,1,1,1,0,0,1],
#               [1,1,0,0,1,0,1,0,1],
#               [1,1,0,1,0,1,0,1,0],
#               [0,0,0,1,1,0,1,1,0],
#               [0,0,0,1,1,0,1,0,1],
#               [0,1,1,0,1,0,1,0,1],
#               [1,0,1,1,0,0,0,0,1],
#               [0,0,1,0,1,0,1,0,1],
#               [0,0,1,1,0,0,0,1,0],
#               [0,0,1,1,1,1,0,0,1]]

# #GENERACION 2
# individuos = [[0,0,1,1,0,1,0,0,1],
#               [0,0,0,1,1,1,0,1,0],
#               [1,1,0,1,0,1,0,1,0],
#               [0,0,0,0,1,0,1,0,1],
#               [0,0,1,1,1,1,0,0,1],
#               [0,1,1,1,1,1,0,0,1],
#               [1,1,0,0,1,0,1,0,1],
#               [0,1,0,1,0,0,0,0,1],
#               [1,0,0,0,1,0,1,0,1],
#               [0,0,0,0,1,0,1,0,1],
#               [0,1,1,0,1,0,1,0,1],
#               [0,1,0,1,1,1,0,1,0],
#               [1,1,0,1,0,1,0,1,0]]

#GENERACION 2
individuos = [[1,1,0,0,1,0,1,0,1],
              [0,1,1,0,1,0,1,0,1],
              [0,1,1,1,0,1,0,1,0],
              [1,0,0,1,1,1,0,0,1],
              [0,1,1,1,0,1,0,1,0],
              [0,1,0,0,1,0,1,0,1],
              [0,0,1,1,1,1,0,1,0],
              [1,1,0,0,1,0,1,0,1],
              [0,0,0,0,1,0,1,0,1],
              [0,0,0,1,0,1,0,1,0],
              [1,1,0,1,0,1,0,1,0],
              [1,1,0,1,0,1,0,1,0],
              [1,1,0,0,1,0,1,0,1]]

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
        xmax = int(9)
        xmin = int(1)
        x = xmin + vcad * ( (xmax - xmin) / (2**9 -1))
        real.append(x)
        adap = (8 * (math.sin(x)) + (5 * (x)))
        adap = ((8 * math.cos(x)) + (x)+(5* (x*x)))
        adaptado.append(adap)

sumatoria = 2072.49142492458

def impresiones():
    for b,d, x, adap in zip(listaprueba, decimal, real, adaptado):
        print(f"\nEl binario es: {b}")
        print(f"El decimal es: {d}")
        #print("El binario ingresado es: " + str(binario) + "\n")
        #print("En decimal seria " + str(binario_decimal(binario)) + "\n")
        print("El real sería " + str(x))
        print("El adaptado sería " + str(adap))
        print("La ruleta sería", (adap*100) / sumatoria, "\n" + "\n")
        
binario_cadena(binario)
binario_decimal()
Vcad()
impresiones()
"""FIN PROGRAMA 1"""


# """RULETA"""


# manzanas = [20,10,25,30]
# nombres = ["Ana","Juan","Diana","Catalina"]
# plt.pie(manzanas, labels=nombres, autopct="%0.1f %%")
# plt.axis("equal")
# plt.show()



# individuos = [5.67,13.04,1.82,1.31,21.3,23.03,1.26,1.25,7.24,17.26,1.82,2.13,2.81]

# nombres = ["Cromosoma1","Cromosoma2""Cromosoma3","Cromosoma4","Cromosoma5","Cromosoma6","Cromosoma7","Cromosoma8","Cromosoma9","Cromosoma10","Cromosoma11","Cromosoma12","Cromosoma13"]
# plt.pie(individuos, labels=nombres)
# plt.show()

# for x in individuos:
#   print(x)  
  
# """FIN RULETA"""



# """Cruce"""
# def CruceDeUnPunto(parent1,parent2,point):
#     p1,p2 = list(parent1),list(parent2) #Convertir string a entero
#     for i in range(point,len(p1)):
#         p1[i],p2[i] = p2[i],p1[i]       #Información genetica
#     p1,p2 = ''.join(p1),''.join(p2)     #Convertir lista a string
#     return p1,p2

# parent1 = input("Ingresa el primer padre: ")      #Cromosomas de los padres
# parent2 = input("Ingresa el segundo padre: ")

# print('Parent1:',parent1)
# print('Parent2:',parent2)
# print("\n")

# point = 5  #Punto de Cruce en bits

# print('Punto de Cruce: ',point)
# print("\n")

# hijo1,hijo2 = CruceDeUnPunto(parent1,parent2,point)

# print('Hijo 1:',hijo1)         #Cromosomas de Hijo
# print('Hijo 2:',hijo2)

# """FIN Cruce"""