import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_civil(
nbr_ci_id  	   NUMBER PRIMARY KEY , 
var_ci_nombre	   VARCHAR2(50) NOT NULL, 
var_ci_status 	   VARCHAR2(50) NOT NULL,
nbr_ba_id    	   NUMBER REFERENCES tb_barrio(nbr_ba_id)
 )
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_civil.csv')

# Insertar datos en tabla
data.to_sql('tb_civil', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_civil
    """
    result = conn.execute(sql)
    for row in result:
        print(row)