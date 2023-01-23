import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_policia(
nbr_pol_id  NUMBER PRIMARY KEY , 
var_pol_nombre	   VARCHAR2(50) NOT NULL, 
var_pol_cargo      	   VARCHAR2(50) NOT NULL, 
var_pol_salario    	   VARCHAR2(50) NOT NULL, 
var_pol_status 	   	   VARCHAR2(50) NOT NULL
)
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_Policia.csv')

# Insertar datos en tabla
data.to_sql('tb_policia', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_policia
    """
    result = conn.execute(sql)
    for row in result:
        print(row)