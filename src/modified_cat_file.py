'''
Scrip que realiza los cambios al archivo catalogo
para que todos tengan el mismo formato.
'''
import pandas as pd 

Catálogo_ORIGEN = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo ORIGEN')
Catálogo_SECTOR = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo SECTOR')
Catálogo_SEXO = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo SEXO')
Catálogo_TIPO_PACIENTE = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo TIPO_PACIENTE')
Catálogo_SI_NO = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo SI_NO')
Catálogo_NACIONALIDAD = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo NACIONALIDAD')
Catálogo_RESULTADO_LAB = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo RESULTADO_LAB',skiprows=1)
Catálogo_RESULTADO_ANTIGENO = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo RESULTADO_ANTIGENO',skiprows=1)
Catálogo_CLASIFICACION_FINAL = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo CLASIFICACION_FINAL',skiprows=2)
Catálogo_ENTIDADES = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo de ENTIDADES')
Catálogo_MUNICIPIOS = pd.read_excel("./Insumos/201128 Catalogos.xlsx",sheet_name='Catálogo MUNICIPIOS')


with pd.ExcelWriter('./Insumos/201128 Catalogos.xlsx') as writer:
    Catálogo_ORIGEN.to_excel(writer, sheet_name='Catálogo ORIGEN',index=False)
    Catálogo_SECTOR.to_excel(writer, sheet_name='Catálogo SECTOR',index=False)
    Catálogo_SEXO.to_excel(writer, sheet_name='Catálogo SEXO',index=False)
    Catálogo_TIPO_PACIENTE.to_excel(writer, sheet_name='Catálogo TIPO_PACIENTE',index=False)
    Catálogo_SI_NO.to_excel(writer, sheet_name='Catálogo SI_NO',index=False)
    Catálogo_NACIONALIDAD.to_excel(writer, sheet_name='Catálogo NACIONALIDAD',index=False)
    Catálogo_RESULTADO_LAB.to_excel(writer, sheet_name='Catálogo RESULTADO_LAB',index=False)
    Catálogo_RESULTADO_ANTIGENO.to_excel(writer, sheet_name='Catálogo RESULTADO_ANTIGENO',index=False)
    Catálogo_CLASIFICACION_FINAL.to_excel(writer, sheet_name='Catálogo CLASIFICACION_FINAL',index=False)
    Catálogo_ENTIDADES.to_excel(writer, sheet_name='Catálogo de ENTIDADES',index=False)
    Catálogo_MUNICIPIOS.to_excel(writer, sheet_name='Catálogo MUNICIPIOS',index=False)