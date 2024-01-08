#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:43:16 2022

@author: alan
"""

"""
Created on Tue Aug 23 10:43:12 2022

@author: hsim17
"""

def CruceDeUnPunto(parent1,parent2,point):
    p1,p2 = list(parent1),list(parent2) #Convertir string a entero
    for i in range(point,len(p1)):
        p1[i],p2[i] = p2[i],p1[i]       #Información genetica
    p1,p2 = ''.join(p1),''.join(p2)     #Convertir lista a string
    return p1,p2

parent1 = input("Ingresa el primer padre: ")      #Cromosomas de los padres
parent2 = input("Ingresa el segundo padre: ")

print('Parent1:',parent1)
print('Parent2:',parent2)
print("\n")

point = 5  #Punto de Cruce en bits

print('Punto de Cruce: ',point)
print("\n")

hijo1,hijo2 = CruceDeUnPunto(parent1,parent2,point)

print('Hijo 1:',hijo1)         #Cromosomas de Hijo
print('Hijo 2:',hijo2)


# individuos = [0,1,0,1,0,0,1,0,1],[0,1,1,0,1,0,1,0,0],[0,0,1,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0],[0,0,1,1,0,1,1,1,0],[0,0,1,1,1,0,1,0,1]















# import random

# def CruceDeUnPunto(l, q):
# 	l = list(l)
# 	q = list(q)
# 	k = random.randint(0, 15)
# 	print("Punto de cruce :", 6)
# # Intercambio de genes
# 	for i in range(k, len(s)):
# 		l[i], q[i] = q[i], l[i]
# 	l = ''.join(l)
# 	q = ''.join(q)
# 	print(l)
# 	print(q, "\n\n")
# 	return l, q


# # Cromosomas

# s = input(str("Ingresa el Primer Binario: "))
# p = input(str("Ingresa el Segundo Binario: "))
# print("\n")

# # individuos = [0,1,0,1,0,0,1,0,1],[0,1,1,0,1,0,1,0,0],[0,0,1,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0],[0,0,1,1,0,1,1,1,0],[0,0,1,1,1,0,1,0,1]

# print("Padres")
# print("P1 :", s)
# print("P2 :", p, "\n")

# # function calling and storing the off springs for
# # next generation CruceDeUnPunto


# for i in range(1):
#     print("Generación ", i+1, "de Hijos :")
#     print("\n")
#     s, p = CruceDeUnPunto(s, p)

# # print("Generación 1 ", "de Hijos :")
# # s, p = CruceDeUnPunto(s, p)
