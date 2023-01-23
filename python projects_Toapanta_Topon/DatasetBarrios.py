'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users=5000

# Generar 4 atributos de la entidad Barrios
features = [
    "nbr_ba_id",
    "var_ba_nombre",    
    "var_ba_status ",
    "nbr_pol_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante la libreria uuid se implementa un ID al Barrio, 
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

'''Se creo un arrelgo que poseea los Barrios. 
Con ayuda de random.choices se asigno un procentaje para cada barrio de la ciudad de la provincia de pichincha.
Esto determina en numero de veces que aparece cada uno. Aquí se le asigno mayor probabilidad de los Barrios 
puesto que, es la zona donde vamos a desarrollar el proyecto'''

barrio = ["Carcelén","El Condado","Cotocollao","Ponceano","Comité del Pueblo","Kennedy","Cochapamba","La Concepción","Jipijapa","Iñaquito","Rumipamba","Belisario Quevedo",
"Mariscal Sucre","San Juan","Centro Histórico","La Libertad","Itchimbía","Puengasí","La Magdalena","Chimbacalle","San Bartolo","Chilibulo","La Ferroviaria","La Argelia",
"La Mena","Solanda","Chillogallo","Quitumbe","La Ecuatoriana","Guamaní","Turubamba","Calderón","San Roque","San Diego"
]
df['var_ba_nombre'] = random.choices(
    barrio, 
    weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,60), 
    k=num_users
)

'''se implementara el estatus del barrio'''

Estado = ["En vigencia", "No existe"]
#Con ayuda de random.choices de establecio el estatus
df['var_ba_status '] = random.choices(
    Estado, 
    weights=(97,3), 
    k=num_users
)

'''Mediante un contador se implementa un ID de los policias, 
el cual va a ser único para cada dato'''
def policia_id ():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_pol_id'] = policia_id()
print(df['nbr_pol_id'].nunique()==num_users)

#Creación del dataset
df.to_csv('dataset_BARRIO.csv')

#Visualización del dataset
pd.read_csv('dataset_BARRIO.csv', index_col=0)