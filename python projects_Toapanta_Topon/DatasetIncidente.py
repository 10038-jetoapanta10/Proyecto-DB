'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users = 5000

# Generar 5 atributos de la entidad Incidente
features = [
    "nbr_inc_id",
    "var_inc_nombre",
    "var_inc_fecha",
    "var_inc_status",
    "nbr_ci_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def incidente_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_inc_id'] = incidente_id()
print(df['nbr_inc_id'].nunique()==num_users)

# Instanlando faker
faker = Faker()
def incidente_nombre():
    return faker.last_name_nonbinary()
df['var_inc_nombre'] = [incidente_nombre() for i in range(num_users)]

# Instanlando faker
faker = Faker()
def incidente_Fecha():
    return faker.date_this_decade()
df['var_inc_fecha'] = [incidente_Fecha() for i in range(num_users)]

#Se asgino un estatus mediante un dato categorico demostrarndo si el delincuente esta vigente o no existe
Estado = ["Caso activo", "Caso cerrado","Caso Archivado"]

#Con ayuda de random.choices de establecio el estatus
df['var_inc_status'] = random.choices(
    Estado, 
    weights=(50,20,30), 
    k=num_users
)

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

#Creación del dataset
df.to_csv('dataset_incidente.csv')
#Visualización del dataset
pd.read_csv('dataset_incidente.csv', index_col=0)