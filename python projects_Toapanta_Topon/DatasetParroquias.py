'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users = 5000
# Generar 6 atributos de la entidad Parroquias
features = [
    "nbr_parro_id",
    "var_parro_nombre",
    "var_parro_status",
    "nbr_can_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)
'''Mediante un contador se implementa un ID a las parroquias, 
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
'''Se creo un arrelgo que poseea las parroquias. 
Con ayuda de random.choices se asigno un procentaje para cada parroquia.
Esto determina en numero de veces que aparece cada uno. Aquí se le asigno mayor probabilidad de la parroquia 
puesto que, es la zona donde vamos a desarrollar el proyecto'''

parroq = ["Belisario Quevedo","Carcelén","Centro Histórico","Chilibulo","Chillogallo","Chimbacalle","Cochapamba","Comité Pueblo",
          "Concepción","Cotocollao", "El Condado","El Inca","Guamaní","Iñaquito","Itchimbía","Jipijapa","Kennedy",
          "La Argelia","La Ecuatoriana","La Ferroviaria","La Libertad","La Mena","Magdalena","Mariscal Sucre","Ponceano","Puengasí",
          "Quitumbe","Rumipamba","San Bartolo","San Juan",'Solanda',"Turubamba"
]
df['var_parro_nombre'] = random.choices(
    parroq, 
    weights=(1,1,40,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,30,1,1,1,1,1,1,1,1,1,1,1), 
    k=num_users
)
#Se asgino un estatus mediante un dato categorico demostrarndo si esta vigente o no existe
#Con ayuda de random.choices de establecio el estatus
Estado = ["En vigencia", "No existe"]
df['var_parro_status'] = random.choices(
    Estado, 
    weights=(98,2), 
    k=num_users
)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def cantonid():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1 
  return L

df['nbr_can_id'] = cantonid()
print(df['nbr_can_id'].nunique()==num_users)

#Creación del dataset
df.to_csv('dataset_parroquia.csv')

#Visualización del dataset
pd.read_csv('dataset_parroquia.csv', index_col=0)