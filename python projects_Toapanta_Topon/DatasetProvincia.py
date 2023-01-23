'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users = 5000

# Generar 4 atributos de la entidad Provincias
features = [
    "nbr_pro_id",
    "var_pro_nombre",
    "var_pro_status",
    "nbr_coor_id"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def provincia_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_pro_id'] = provincia_id()
print(df['nbr_pro_id'].nunique()==num_users)


'''Se creo un arrelgo que poseea las 24 provincicias de Ecuador. 
Con ayuda de random.choices se asigno un procentaje para cada provincia.
Esto determina en numero de veces que apare cada una. Aquí se le asigno mayor probabilidad a la provincia de pichincha 
puesto que, es la zona donde vamos a desarrollar el proyecto'''

Provincias = ["Esmeraldas","Manabí","Los Ríos","Santa Elena","Guayas","Santo Domingo de los Tsáchilas","El Oro","Azuay",
              "Bolívar","Cañar","Carchi","Cotopaxi","Chimborazo","Imbabura","Loja","Pichincha","Tungurahua", "Morona Santiago",
              "Napo","Orellana","Pastaza","Sucumbíos","Zamora Chinchipe","Galapagos"]

df['var_pro_nombre'] = random.choices(
    Provincias, 
    weights=(3,3,3,3,4,3,3,4,3,4,4,4,3,3,3,20,4,4,4,4,4,4,3,3), 
    k=num_users
)

#Se asgino un estatus mediante un dato categorico demostrarndo si la provincia esta vigente o no existe
Estado = ["En vigencia", "No existe"]

#Con ayuda de random.choices de establecio el estatus
df['var_pro_status'] = random.choices(
    Estado, 
    weights=(97,3), 
    k=num_users
)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def coord_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_coor_id'] = coord_id()
print(df['nbr_coor_id'].nunique()==num_users)


#Creación del dataset
df.to_csv('dataset_Prov.csv')

#Visualización del dataset
pd.read_csv('dataset_Prov.csv', index_col=0)