#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:25:33 2022

@author: hsim17
"""

# realizar un programa que emule el proceso de seleccion ruleta
# ordenar en base a su aptitud

import matplotlib.pyplot as plt

individuos = [63.30,27.03,22.55,15.20,13.92,13.51,8.82]
nombres = ["individuo 1", "individuo 2","individuo 3","individuo 4","individuo 5","individuo 6","individuo 7",]
plt.pie(individuos, labels=nombres)
plt.show()

for x in individuos:
  print(x)
  
  
"""Apunte"""
#Un algortimo genetico va a converger cuando se especifica el numero de generaciones a iterar
#Cuando se especifique y se saisfaga el llegar a la formula
# El medio ambiente o funcion de adaptación