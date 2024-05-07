'''
Script que genera la carga del catalogo de entidades 
y municipios a nuestra BD
'''
#import polars as pd
import pandas as pd
import psycopg2 as ps

catalogo_master = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo MUNICIPIOS')
catalogo_entidades = pd.read_excel("./Insumos/201128 Catalogos.xlsx",
                                   sheet_name='Catálogo de ENTIDADES')

aguascalientes = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 1]
baja_california = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 2]
baja_california_sur = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 3]
campeche = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 4]
coahuila = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 5]
colima = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 6]
chiapas = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 7]
chihuahua = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 8]
ciudad_de_mexico = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 9]
durango = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 10]
guanajuato = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 11]
guerrero = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 12]
hidalgo = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 13]
jalisco = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 14]
mexico = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 15]
michoacan = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 16]
morelos = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 17]
nayarit = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 18]
nuevo_leon = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 19]
oaxaca = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 20]
puebla = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 21]
queretaro = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 22]
quintana_roo = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 23]
san_luis_potosi = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 24]
sinaloa = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 25]
sonora = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 26]
tabasco = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 27]
tamaulipas = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 28]
tlaxcala = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 29]
veracruz = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 30]
yucatan = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 31]
zacatecas = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 32]
eum = catalogo_master[catalogo_master['CLAVE_ENTIDAD'] == 36]

name_mun_list = [aguascalientes,baja_california,baja_california_sur,campeche,
                 coahuila,colima,chiapas,chihuahua,ciudad_de_mexico,durango,
                 guanajuato,guerrero,hidalgo,jalisco,mexico,michoacan,morelos,
                 nayarit,nuevo_leon,oaxaca,puebla,queretaro,quintana_roo,
                 san_luis_potosi,sinaloa,sonora,tabasco,tamaulipas,tlaxcala,
                 veracruz,yucatan,zacatecas,eum]

estados_name =  ['aguascalientes','baja_california','baja_california_sur','campeche',
                 'coahuila','colima','chiapas','chihuahua','ciudad_de_mexico','durango',
                 'guanajuato','guerrero','hidalgo','jalisco','mexico','michoacan','morelos',
                 'nayarit','nuevo_leon','oaxaca','puebla','queretaro','quintana_roo',
                 'san_luis_potosi','sinaloa','sonora','tabasco','tamaulipas','tlaxcala',
                 'veracruz','yucatan','zacatecas','eum']


def connect_to_postgres():
    '''
    establece los parametros para establecer la conexion a postgres
    '''

    host_name = 'localhost'
    dbname = "coursedb"
    port = 5435
    username = "alumno"
    password = 123456

    try:
        connexion = ps.connect(host=host_name, dbname=dbname, user=username
                          ,password=password, port=port)
    except ps.OperationalError as e:
        raise e
    else:
        print('conexion exitosa')
        return connexion

def insert_data_mun(curr,clave_municipio,municipio,clave_entidad,table):
    '''
    inserta los registros correspondientes al cat municipio
    '''
    insertar_raw_data = f"""INSERT INTO estados.{table} (clave_municipio,municipio,clave_entidad) VALUES(%s,%s,%s);"""
    insertando_row = (clave_municipio,municipio,clave_entidad)
    curr.execute(insertar_raw_data, insertando_row)

def insert_data_ent(curr,clave_municipio,municipio,clave_entidad,table):
    '''
    inserta los registros correspondientes al cat entidades
    '''
    insertar_raw_data = f"""INSERT INTO estados.{table} (clave_entidad,entidad_federativa,abreviatura) VALUES(%s,%s,%s);"""
    insertando_row = (clave_municipio,municipio,clave_entidad)
    curr.execute(insertar_raw_data, insertando_row)

def add_to_postgres_mun(curr,key_1,key_2,key_3,df,table):
    '''
    realiza la carga de los datos del cat municipio a postgres
    '''
    for _, row in df.iterrows():
        insert_data_mun(curr,row[key_1],row[key_2],row[key_3],table)


def add_to_postgres_ent(curr,key_1,key_2,key_3,df,table):
    '''
    realiza la carga de los datos del cat entidades a postgres
    '''
    for _, row in df.iterrows():
        insert_data_ent(curr,row[key_1],row[key_2],row[key_3],table)


conn = connect_to_postgres()
curr = conn.cursor()

for element in range(len(name_mun_list)):
    add_to_postgres_mun(curr,'CLAVE_MUNICIPIO','MUNICIPIO','CLAVE_ENTIDAD',
                         name_mun_list[element],f'{estados_name[element]}')

add_to_postgres_ent(curr,'CLAVE_ENTIDAD','ENTIDAD_FEDERATIVA','ABREVIATURA'
                     ,catalogo_entidades,'entidades')


conn.commit()

curr.close()
conn.close()
