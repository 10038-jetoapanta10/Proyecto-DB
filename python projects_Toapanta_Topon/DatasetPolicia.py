'''Primero importamos todas las librerias 
que vamos a utilizar'''
import uuid
import pandas as pd
import random
from faker import Faker
import datetime

#Numero de datos a obtener
num_users=5000

# Generar 5 atributos de la entidad policia
features = [
    "nbr_pol_id",
    "var_pol_nombre",
    "var_pol_cargo",
    "var_pol_salario",
    "var_pol_status"

]# Creating a DF for these features
df = pd.DataFrame(columns=features)

'''Mediante un contador se implementa un ID, 
el cual va a ser unico para cada dato'''
def policia_id():
  i=1
  L=[]
  while i<=num_users:
    L.append(i)
    i=i+1
    
  return L

df['nbr_pol_id'] = policia_id()
print(df['nbr_pol_id'].nunique()==num_users)

'''Estado de actividad de los policias'''
policia_status = ["Activo", "Inactivo"]

df['var_pol_status'] = random.choices(
    policia_status, 
    weights=(65,35), 
    k=num_users
)

# Instantiating faker
faker = Faker()

def policia_nombre():
    return faker.name()
df['var_pol_nombre'] = [policia_nombre() for i in range(num_users)]

''' Se asigna los cargo que tiene los policias que residen en un UPC '''
policia_cargo = ["Sargento", "Cabo" , "Policia"]

df['var_pol_cargo'] = random.choices(
    policia_cargo, 
    weights=(10,30,60), 
    k=num_users
)

'''A cada policia se le asignara el salario en base a su rango o cargo'''
faker = Faker()
def policia_salario (var_pol_cargo):
  if var_pol_cargo=='Sargento':
      salarioS=1250
      return salarioS
  elif var_pol_cargo=='Cabo':
      salarioC=1120
      return salarioC
  elif var_pol_cargo=='Policia':
      salarioP=930
      return salarioP

df['var_pol_salario'] = [policia_salario(i) for i in df['var_pol_cargo']]

#Creación del dataset
df.to_csv('dataset_Policia.csv')

#Visualización del dataset
pd.read_csv('dataset_Policia.csv', index_col=0)