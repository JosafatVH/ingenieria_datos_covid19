'''

Script encargado de bajar los archivos/insumos
que el gobierno de la Ciudad de México pone a 
disposicion sobre los casos registrados de covid19

'''
import zipfile
from pathlib import Path
import urllib.request

def create_folder():
    '''
    Genera la carpeta Insumos
    '''
    rute = Path("Insumos")
    rute.mkdir()

def data_covid():
    '''
    Descarga el archivo con los registros del covid y lo deposita en la carpeta insumos
    '''
    url_data = 'https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'
    url_dict = 'https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip'
    name_data = 'Insumos/datos_abiertos_covid19.zip'
    name_dict = 'Insumos/diccionario_datos_covid19.zip'

    urllib.request.urlretrieve(url_data, name_data)
    urllib.request.urlretrieve(url_dict, name_dict)

def unzip_file():
    '''
    Descomprime los insumos necesarios.
    '''
    directorio_zip = Path('Insumos')
    archivo_zip = list(directorio_zip.glob("*.zip"))

    for ruta in archivo_zip:
        with zipfile.ZipFile(ruta,'r') as zip_object:
            zip_object.extractall(path=directorio_zip)

create_folder()
data_covid()
unzip_file()
