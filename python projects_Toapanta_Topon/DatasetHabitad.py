'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users=5000

# Generar 4 atributos de la entidad Habitad
features = [
    "nbr_hab_id",
    "var_hab_descripcion",
    "nbr_upc_id",    
    "nbr_pol_id",
    
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def habitad_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_hab_id'] = habitad_id()
print(df['nbr_hab_id'].nunique()==num_users)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def upc_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_upc_id'] = upc_id()
print(df['nbr_upc_id'].nunique()==num_users)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def policia_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_pol_id'] = policia_id()
print(df['nbr_pol_id'].nunique()==num_users)

#Se asgino un estatus mediante un dato categorico demostrarndo si el upc es barrial o es un vehíulo(movil)
#Con ayuda de random.choices de establecio el estatus
tipo = ["Barrial", "Movil"]
df['var_hab_descripcion'] = random.choices(
    tipo, 
    weights=(85,15), 
    k=num_users
)

#Creación del dataset
df.to_csv('dataset_habitad.csv')

#Visualización del dataset
pd.read_csv('dataset_habitad.csv', index_col=0)
