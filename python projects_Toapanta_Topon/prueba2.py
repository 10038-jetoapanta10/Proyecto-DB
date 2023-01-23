import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_coordenada(
nbr_coor_id              	NUMBER PRIMARY KEY , 
var_coor_latitud         	VARCHAR2(50) NOT NULL  ,
var_coor_longitud       	VARCHAR2(50) NOT NULL
)
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_Coord.csv')

# Insertar datos en tabla
data.to_sql('tb_coordenada', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_coordenada
    """
    result = conn.execute(sql)
    for row in result:
        print(row)