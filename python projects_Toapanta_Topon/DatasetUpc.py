'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime


#Numero de datos a obtener
num_users=5000

# Generar 4 atributos de la entidad UPC

features = [
    "nbr_upc_id",
    "var_upc_nombre",
    "var_upc_status",
    "nbr_ciu_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

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

'''Mediante la libreria faker se creo un nombres falsos 
para cada UPC '''
faker = Faker()

def Primer_Nom():
    return faker.city()
df['var_upc_nombre'] = [Primer_Nom() for i in range(num_users)]

#Se asgino un estatus mediante un dato categorico demostrarndo si el upc esta activo o inactivo
Estado = ["Activo", "Inactivo"]

#Con ayuda de random.choices de establecio el estatus
df['var_upc_status'] = random.choices(
    Estado, 
    weights=(97,3), 
    k=num_users
)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def cuidad_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1 
  return L
df['nbr_ciu_id'] = cuidad_id()
print(df['nbr_ciu_id'].nunique()==num_users)

#Creación del dataset
df.to_csv('dataset_UPC.csv')

#Visualización del dataset
pd.read_csv('dataset_UPC.csv', index_col=0)