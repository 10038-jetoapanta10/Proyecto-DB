'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users = 5000

# Generar 5 atributos para la entidad delincuente
features = [
    "nbr_delin_id",
    "var_delin_nombre",
    "var_delin_pandilla",
    "var_delin_apodo",
    "var_delin_status"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
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

# Instanlando faker
''' Se genera nombres falsos para el delincuente '''
faker = Faker()
def delincuente_nombre():
    return faker.name()
df['var_delin_nombre'] = [delincuente_nombre() for i in range(num_users)]

# Instanlando faker
''' Se genera nombres falsos para las pandillas del barrio '''
faker = Faker()
def delincuente_pandilla():
    return faker.city_prefix()
df['var_delin_pandilla'] = [delincuente_pandilla() for i in range(num_users)]

# Instanlando faker
''' Se genera apodos falsos para los delincuentes '''
faker = Faker()
def delincuente_pandilla1():
    return faker.domain_word()
df['var_delin_apodo'] = [delincuente_pandilla1() for i in range(num_users)]

#Se asgino un estatus mediante un dato categorico demostrarndo si el delincuente esta Activo o no Activo
Estado = ["Activo", "No Activo"]

#Con ayuda de random.choices de establecio el estatus
df['var_delin_status'] = random.choices(
    Estado, 
    weights=(97,3), 
    k=num_users
)

#Creación del dataset
df.to_csv('dataset_delincuentes.csv')
#Visualización del dataset
pd.read_csv('dataset_delincuentes.csv', index_col=0)





