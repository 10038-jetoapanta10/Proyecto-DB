import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_ciudad(
nbr_ciu_id       		NUMBER PRIMARY KEY , 
var_ciu_nombre	VARCHAR2(50) NOT NULL, 
var_ciu_status 	   	VARCHAR2(50) NOT NULL,
nbr_parro_id   		NUMBER REFERENCES tb_parroquia (nbr_parro_id)
 )
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_Ciudad.csv')

# Insertar datos en tabla
data.to_sql('tb_ciudad', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT nbr_ciu_id
        FROM tb_ciudad
    """
    result = conn.execute(sql)
    for row in result:
        print(row)