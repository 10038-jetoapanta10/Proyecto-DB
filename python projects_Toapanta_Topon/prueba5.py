import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_parroquia(
nbr_parro_id   		 NUMBER PRIMARY KEY , 
var_parro_nombre	 VARCHAR2(50) NOT NULL, 
var_parro_status 	 VARCHAR2(50) NOT NULL,
nbr_can_id  		NUMBER REFERENCES tb_canton (nbr_can_id)
 )
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_parroquia.csv')

# Insertar datos en tabla
data.to_sql('tb_parroquia', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_parroquia
    """
    result = conn.execute(sql)
    for row in result:
        print(row)