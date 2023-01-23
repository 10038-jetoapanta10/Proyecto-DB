import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_habitad (
nbr_hab_id  		NUMBER PRIMARY KEY , 
var_hab_descripcion      VARCHAR2(50) NOT NULL, 
nbr_upc_id   		NUMBER REFERENCES tb_upc(nbr_upc_id),
nbr_pol_id  		NUMBER REFERENCES tb_policia(nbr_pol_id)
)
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_habitad.csv')

# Insertar datos en tabla
data.to_sql('tb_habitad', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_habitad
    """
    result = conn.execute(sql)
    for row in result:
        print(row)