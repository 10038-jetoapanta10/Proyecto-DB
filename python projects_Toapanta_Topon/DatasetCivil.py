'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users=5000

# Generar 4 atributos para la entidad Civil
features = [
    "nbr_ci_id",
    "var_ci_nombre",
    "var_ci_status",
    "nbr_ba_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def civil_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_ci_id'] = civil_id()
print(df['nbr_ci_id'].nunique()==num_users)

# Instanlando faker
''' Se genera nombres falsos para el civil '''
faker = Faker()
def delincuente_nombre():
    return faker.name()
df['var_ci_nombre'] = [delincuente_nombre() for i in range(num_users)]

#Se asgino un estatus mediante un dato categorico demostrarndo el estado civil de la persona
Estado = ["solter/a", "casado/a","Viudo/a","Divorciado/a"]

#Con ayuda de random.choices de establecio el estatus
df['var_ci_status'] = random.choices(
    Estado, 
    weights=(44,35,8,13), 
    k=num_users
)

'''Mediante un contador se implementa el ID del barrio, 
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

#Creación del dataset
df.to_csv('dataset_civil.csv')
#Visualización del dataset
pd.read_csv('dataset_civil.csv', index_col=0)