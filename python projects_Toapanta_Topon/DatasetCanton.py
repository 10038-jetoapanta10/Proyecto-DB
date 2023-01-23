'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users = 5000

# Generar 4 atributos de la entidad Cantones

features = [
    "nbr_can_id",
    "can_Nombre",
    "can_Status",
    "can_IdProvincia"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante la libreria uuid se implementa un ID a los Cantones, 
el cual va a ser único para cada dato'''

def cantonid():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1 
  return L

df['nbr_can_id'] = cantonid()
print(df['nbr_can_id'].nunique()==num_users)

'''Se creo un arrelgo que poseea los cantones de la provincia de Pichincha. 
Con ayuda de random.choices se asigno un procentaje para cada canton.
Esto determina en numero de veces que aparece cada uno. Aquí se le asigno mayor probabilidad al canton del Distrito Metropolitano de Quito 
puesto que, es la zona donde vamos a desarrollar el proyecto'''

canton = ["Cayambe","Distrito Metropolitano de Quito","Mejia","Pedro Moncayo", "Pedro Vicente Maldonado","Puerto Quito","Rumiñahui","San Miguel de los Bancos"]
df['can_Nombre'] = random.choices(
    canton, 
    weights=(5,65,5,5,5,5,5,5), 
    k=num_users
)

#Se asgino un estatus mediante un dato categorico demostrarndo si la provincia esta vigente o no existe
#Con ayuda de random.choices de establecio el estatus
estadoC = ["En vigencia", "No existe"]
df['can_Status'] = random.choices(
    estadoC, 
    weights=(97,3), 
    k=num_users
)

'''Mediante la libreria uuid se implementa un ID
el cual va a ser único para cada dato'''

def provincia_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['can_IdProvincia'] = provincia_id()
print(df['can_IdProvincia'].nunique()==num_users)

#Creación del dataset
df.to_csv('dataset_Canton.csv')
#Visualización del dataset
pd.read_csv('dataset_Canton.csv', index_col=0)