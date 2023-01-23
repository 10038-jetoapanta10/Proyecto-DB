'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users = 5000

# Generar 3 atribustos de la entidad Coordenandas
features = [
    "nbr_coor_id",
    "var_coor_latitud",
    "var_coor_longitud "
]# Creating a DF for these features
df = pd.DataFrame(columns=features)

'''Mediante la libreria uuid se implementa un ID a Coordenadas, 
el cual va a ser unico para cada dato'''
def coorid():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
  return L

df['nbr_coor_id'] = coorid()
print(df['nbr_coor_id'].nunique()==num_users)

'''En base  a nuestro problema, 
la Latitud estan asignadas a la direccion del sector que vamos a trabajar, 
provincia de pichicncha, ciudad quito, sector centro (Basadas en WGS 84)'''
df['var_coor_latitud']= [random.uniform(-0,0.9)for i in range(num_users)]


'''En base  a nuestro problema, 
la longitud estan asignadas a la direccion del sector que vamos a trabajar, 
provincia de pichicncha, ciudad quito, sector centro (Basadas en WGS 84)'''
df['var_coor_longitud ']= [random.uniform(79,78)for i in range(num_users)]

#Creación del dataset
df.to_csv('dataset_Coord.csv')

#Visualización del dataset
pd.read_csv('dataset_Coord.csv', index_col=0)