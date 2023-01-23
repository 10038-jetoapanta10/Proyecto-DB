import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_delincuente(
nbr_delin_id  NUMBER PRIMARY KEY , 
var_delin_nombre	   VARCHAR2(50) NOT NULL,
var_delin_pandilla    	   VARCHAR2(50) NOT NULL,
var_delin_apodo     	   VARCHAR2(50) NOT NULL,
var_delin_status 	   VARCHAR2(50) NOT NULL
 )
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_delincuentes.csv')

# Insertar datos en tabla
data.to_sql('tb_delincuente', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_delincuente
    """
    result = conn.execute(sql)
    for row in result:
        print(row)