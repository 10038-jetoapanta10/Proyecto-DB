'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users=5000
# Generar 4 atributos de la entidad Ciudad

features = [
    "nbr_ciu_id",
    "var_ciu_nombre",
    "var_ciu_status",
    "nbr_parro_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

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

'''Se creo un arrelgo que poseea las cuidades. 
Con ayuda de random.choices se asigno un procentaje para cada ciudad de la provincia de pichincha.
Esto determina en numero de veces que aparece cada uno. Aquí se le asigno mayor probabilidad de las cuidades 
puesto que, es la zona donde vamos a desarrollar el proyecto'''

ciudad = ["Aloag","Cayambe","Machachi","Quito","San Miguel De Los Bancos","Sangolquí","Tabacundo"
]
df['var_ciu_nombre'] = random.choices(
    ciudad, 
    weights=(5,5,5,70,5,5,5), 
    k=num_users
)

#Se asgino un estatus mediante un dato categorico demostrarndo si esta vigente o no existe
#Con ayuda de random.choices de establecio el estatus
Estado = ["En vigencia", "No existe"]
df['var_ciu_status'] = random.choices(
    Estado, 
    weights=(98,2), 
    k=num_users
)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''

def parroquia_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L
df['nbr_parro_id'] = parroquia_id()
print(df['nbr_parro_id'].nunique()==num_users)

#Creación del dataset
df.to_csv('dataset_Ciudad.csv')

#Visualización del dataset
pd.read_csv('dataset_Ciudad.csv', index_col=0)