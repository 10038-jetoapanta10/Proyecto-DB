'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users=5000

# Generar 4 atributos de la entidad Asaltar
features = [
    "nbr_asl_id",
    "var_asl_forma_asaltar",
    "nbr_ba_id",
    "nbr_delin_id"
]# Creating a DF for these features
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def asalto_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_asl_id'] = asalto_id()
print(df['nbr_asl_id'].nunique()==num_users)


#Se asginó un estatus mediante un dato categorico demostrarndo los tipos de asaltos que ocurren en el barrio

estado = ["Con armas de fuego", "Con armas cortopulsante", "Extorsion", "Dulces sueños"]

df['var_asl_forma_asaltar'] = random.choices(
    estado, 
    weights=(55,25,5,15), 
    k=num_users
)

'''Mediante un contador se implementa el ID de Barrio, 
el cual va a ser unico para cada dato'''
def barrio_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_ba_id'] = barrio_id()
print(df['nbr_ba_id'].nunique()==num_users)

'''Mediante un contador se implementa el ID del delincuente, 
el cual va a ser unico para cada dato'''
def delincuente_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_delin_id'] = delincuente_id()
print(df['nbr_delin_id'].nunique()==num_users)

#Creación del dataset
df.to_csv('dataset_asaltar.csv')
#Visualización del dataset
pd.read_csv('dataset_asaltar.csv', index_col=0)

