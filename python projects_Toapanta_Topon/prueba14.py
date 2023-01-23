import pandas as pd
from sqlalchemy import create_engine

# Crear tabla en Oracle XE
engine = create_engine('oracle+cx_oracle://SYSTEM:Superat1234@localhost:1521/xe')
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE tb_asaltar (
nbr_asl_id  		NUMBER PRIMARY KEY , 
var_asl_forma_asaltar   VARCHAR2(50) NOT NULL, 
nbr_ba_id  		NUMBER REFERENCES tb_barrio(nbr_ba_id),
nbr_delin_id   		NUMBER REFERENCES tb_delincuente (nbr_delin_id)
)
    """)

# Cargar dataset desde archivo CSV
data = pd.read_csv('dataset_asaltar.csv')

# Insertar datos en tabla
data.to_sql('tb_asaltar', engine, if_exists='append', index=False)

# Unir tablas
with engine.connect() as conn:
    sql = """
        SELECT *
        FROM tb_asaltar
    """
    result = conn.execute(sql)
    for row in result:
        print(row)