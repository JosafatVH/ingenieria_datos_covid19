'''
Script para cargar la informacion de los catalogos a 
nuestra BD en postgresql
'''
import pandas as pd
import psycopg2 as ps

cat_master = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name=None)
class_final = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo CLASIFICACION_FINAL')

name_cat_list = ['Catálogo ORIGEN','Catálogo SECTOR','Catálogo SEXO','Catálogo TIPO_PACIENTE',
                 'Catálogo SI_NO','Catálogo NACIONALIDAD','Catálogo RESULTADO_LAB'
                 ,'Catálogo RESULTADO_ANTIGENO']

table_names = ['cat_origen','cat_sector','sexo','tipo_paciente','si_no',
               'nacionalidad','resultado_lab','resultado_antigeno']

def connect_to_postgres():
    '''
    se establecen los parametros para poder realizar la conexion a postgresql
    '''
    host_name = 'localhost'
    dbname = "coursedb"
    port = 5435
    username = "alumno"
    password = 123456

    try:
        conx = ps.connect(host=host_name, dbname=dbname, user=username
                          ,password=password, port=port)
    except ps.OperationalError as e:
        raise e
    else:
        print('conexion exitosa')
        return conx
    
def insert_cat_data(curr,clave,descripcion,table):
    '''
    Se genera la informacion a insertar en nuestras tablas
    '''
    insertar_raw_data = f"""INSERT INTO raw_data.{table} (clave,descripcion) VALUES(%s,%s);"""
    insertando_row = (clave,descripcion)
    curr.execute(insertar_raw_data, insertando_row)

def insert_class_final(curr,clave,clasificacion,descripcion):
    insertar_raw_data_final = """INSERT INTO raw_data.clasificacion_final (clave,clasificacion,descripcion) VALUES(%s,%s,%s);"""
    insertando_row = (clave,clasificacion,descripcion)
    curr.execute(insertar_raw_data_final, insertando_row)

def add_to_postgres(curr,key_1,key_2,df,table):
    '''
    Manda los datos a insertar a nuestra base en postgresql
    '''
    name_cat = cat_master[f"{df}"]
    for _, row in name_cat.iterrows():
        insert_cat_data(curr,row[key_1],row[key_2],table)

def add_to_postgres_class(curr,key_1,key_2,key_3,df):
    '''
    Manda los datos a insertar a nuestra base en postgresql
    '''
    for _, row in df.iterrows():
        insert_class_final(curr,row[key_1],row[key_2],row[key_3])



conn = connect_to_postgres()
curr = conn.cursor()

add_to_postgres_class(curr,'CLAVE','CLASIFICACIÓN','DESCRIPCIÓN',class_final)


for element in range(len(name_cat_list)):
    add_to_postgres(curr,'CLAVE','DESCRIPCIÓN',f'{name_cat_list[element]}'
                 ,f'{table_names[element]}')


conn.commit()

curr.close()
conn.close()
