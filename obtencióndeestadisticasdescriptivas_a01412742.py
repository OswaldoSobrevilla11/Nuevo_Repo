# -*- coding: utf-8 -*-
"""Obtencióndeestadisticasdescriptivas_A01412742

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Y9n-eSTtDRyWFviBgW9teiH0ju8uw0u
"""

# Imports
import pandas as pd

#Importar Tabla
df = pd.read_csv("Litros_y_Servicios_ASA_2015-2022.csv")
print(df.head(10))

print(df.describe())

#Media
df.groupby(['Estado ']).mean()

#Mediana
df.groupby(['Estado ']).median()

#Desviacion Estandar
df.groupby(['Estado ']).std()

#Min
df.groupby(['Estado ']).min()

#Max
df.groupby(['Estado ']).max()