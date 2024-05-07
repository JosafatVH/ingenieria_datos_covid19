'''
Script para la carga de los datos del covid19 en México
a nuestra BD
'''
import pandas as pd
import psycopg2 as ps

covid19 = pd.read_csv('./Insumos/COVID19MEXICO.csv')
#covid19 = data.head(100000)

def connect_to_postgres():
    '''
    establece los parametros para realizar la conexion a postgres
    '''
    host_name = 'localhost'
    dbname = "coursedb"
    port = 5435
    username = "alumno"
    password = 123456

    try:
        conx = ps.connect(host=host_name, dbname=dbname,
                          user=username, password=password, port=port)
    except ps.OperationalError as e:
        raise e
    else:
        print('conexion exitosa')
        return conx


def insert_covid_data(curr, fecha_actualizacion, id_registro, origen, sector, entidad_um, sexo,
                       entidad_nac, entidad_res, municipio_res, tipo_paciente, fecha_ingreso, fecha_sintomas,
                       fecha_def, intubado, neumonia, edad, nacionalidad, embarazo, habla_lengua_indig,
                       indigena, diabetes, epoc, asma, inmusupr, hipertension, otra_com, cardiovascular, obesidad,
                       renal_cronica, tabaquismo, otro_caso, toma_muestra_lab, resultado_lab, toma_muestra_antigeno,
                       resultado_antigeno, clasificacion_final, migrante, pais_nacionalidad, pais_origen, uci):
    
    '''
    Inserta los datos del archivo covid
    '''

    insertar_data_covid = """INSERT INTO raw_data.casos_covid (fecha_actualizacion,id_registro,origen,sector,entidad_um,sexo,
                           entidad_nac,entidad_res,municipio_res,tipo_paciente,fecha_ingreso,fecha_sintomas,
                           fecha_def,intubado,neumonia,edad,nacionalidad,embarazo,habla_lengua_indig,
                           indigena,diabetes,epoc,asma,inmusupr,hipertension,otra_com,cardiovascular,obesidad,
                           renal_cronica,tabaquismo,otro_caso,toma_muestra_lab,resultado_lab,toma_muestra_antigeno,
                           resultado_antigeno,clasificacion_final,migrante,pais_nacionalidad,pais_origen,uci)                    
                           VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

    insertando_row = (fecha_actualizacion, id_registro, origen, sector, entidad_um, sexo,
                      entidad_nac, entidad_res, municipio_res, tipo_paciente, fecha_ingreso, fecha_sintomas,
                      fecha_def, intubado, neumonia, edad, nacionalidad, embarazo, habla_lengua_indig,
                      indigena, diabetes, epoc, asma, inmusupr, hipertension, otra_com, cardiovascular, obesidad,
                      renal_cronica, tabaquismo, otro_caso, toma_muestra_lab, resultado_lab, toma_muestra_antigeno,
                      resultado_antigeno, clasificacion_final, migrante, pais_nacionalidad, pais_origen, uci)

    curr.execute(insertar_data_covid, insertando_row)


def add_to_postgres(curr, df):
    '''
    realiza la carga a postgresql
    '''
    for _, row in df.iterrows():
        insert_covid_data(curr, row['FECHA_ACTUALIZACION'], row['ID_REGISTRO'], row['ORIGEN'], row['SECTOR'],
                           row['ENTIDAD_UM'], row['SEXO'], row['ENTIDAD_NAC'], row['ENTIDAD_RES'], row['MUNICIPIO_RES'],
                           row['TIPO_PACIENTE'], row['FECHA_INGRESO'], row['FECHA_SINTOMAS'], row['FECHA_DEF'], row['INTUBADO'],
                           row['NEUMONIA'], row['EDAD'], row['NACIONALIDAD'], row['EMBARAZO'], row['HABLA_LENGUA_INDIG'],
                           row['INDIGENA'], row['DIABETES'], row['EPOC'], row['ASMA'], row['INMUSUPR'], row['HIPERTENSION'], row['OTRA_COM'],
                           row['CARDIOVASCULAR'], row['OBESIDAD'], row['RENAL_CRONICA'], row['TABAQUISMO'], row['OTRO_CASO'],
                           row['TOMA_MUESTRA_LAB'], row['RESULTADO_LAB'], row['TOMA_MUESTRA_ANTIGENO'], row['RESULTADO_ANTIGENO'],
                           row['CLASIFICACION_FINAL'], row['MIGRANTE'], row['PAIS_NACIONALIDAD'], row['PAIS_ORIGEN'], row['UCI']
                           )


conn = connect_to_postgres()
cur = conn.cursor()

add_to_postgres(cur, covid19)

conn.commit()
cur.close()
conn.close()
