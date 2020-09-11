#!/usr/bin/env python3
from ezodf import newdoc
import os
import zipfile
import tempfile
#
def updateZip(zipname, filename, data):
    # This function and general algoritm from:
    # https://stackoverflow.com/questions/30596477/editing-a-odt-file-using-python
    # generate a temp file
    tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
    os.close(tmpfd)

    # create a temp copy of the archive without filename
    with zipfile.ZipFile(zipname, 'r') as zin:
        with zipfile.ZipFile(tmpname, 'w') as zout:
            zout.comment = zin.comment # preserve the comment
            for item in zin.infolist():
                if item.filename != filename:
                    zout.writestr(item, zin.read(item.filename))

    # replace with the temp archive
    os.remove(zipname)
    os.rename(tmpname, zipname)

    # now add filename with its new data
    with zipfile.ZipFile(zipname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(filename, data)
#
def lee_pendientes(filename,sep="|"):
    papiro = []
    with open(filename) as my_file:
        for line in my_file:
            if len(line.strip()) != 0: # Condición de linea (no) vacía
                l=line.strip().split(sep) # "Limpia" los extremos y la pica en pedazos separados por espacios
                #l=list(map(float, l)) # Convierte los elementos en números
                papiro.append(l) # Agrega la fila de números al arreglo
    dim=len(papiro[0])
    print('dim=',dim)
    return(papiro)
#
nombre_generico=['XXX_NOMBRE_ESTUDIANTE_XXX',
'XXX_CEDULA_ESTUDIANTE_XXX',
'XXX_TITULO_TEG_XXX',
'XXX_TITULO_QUE_ASPIRA_XXX',
'XXX_DIA_DEFENSA_XXX',
'XXX_MES_DEFENSA_XXX',
'XXX_ANHO_DEFENSA_XXX',
'XXX_HORA_DEFENSA_XXX',
'XXX_LUGAR_DEFENSA_XXX',
'XXX_DIA_ACTA_XXX',
'XXX_MES_ACTA_XXX',
'XXX_ANHO_ACTA_XXX',
'XXX_COORDINADOR_A_JURADO_XXX',
'XXX_EL_LA_TUTOR_A_XXX',
'XXX_TITULO_TUTOR_XXX',
'XXX_NOMBRE_TUTOR_XXX',
'XXX_ADSCRIPCION_TUTOR_XXX',
'XXX_TITULO_JURADO_1_XXX',
'XXX_NOMBRE_JURADO_1_XXX',
'XXX_ADS_JURADO_1_XXX',
'XXX_TITULO_JURADO_2_XXX',
'XXX_NOMBRE_JURADO_2_XXX',
'XXX_ADS_JURADO_2_XXX']
#
def diccionario(lista_claves,lista_contenido):
    dic={lista_claves[0]:lista_contenido[1],
        lista_claves[1]:lista_contenido[3],
        lista_claves[2]:lista_contenido[4],
        lista_claves[3]:'', #lista_contenido[2]
        lista_claves[4]:lista_contenido[24],
        lista_claves[5]:lista_contenido[25],
        lista_claves[6]:lista_contenido[26],
        lista_claves[7]:lista_contenido[27],
        lista_claves[8]:lista_contenido[28],
        lista_claves[9]:lista_contenido[24],
        lista_claves[10]:lista_contenido[25],
        lista_claves[11]:lista_contenido[26],
        lista_claves[12]:'', #lista_contenido[6],
        lista_claves[13]:'', #lista_contenido[6],
        lista_claves[14]:lista_contenido[7],
        lista_claves[15]:lista_contenido[5],
        lista_claves[16]:lista_contenido[9],
        lista_claves[17]:lista_contenido[11],
        lista_claves[18]:lista_contenido[10],
        lista_claves[19]:lista_contenido[13],
        lista_claves[20]:lista_contenido[15],
        lista_claves[21]:lista_contenido[14],
        lista_claves[22]:lista_contenido[17],
        }
    if lista_contenido[2]=='f':
        dic[lista_claves[3]]='Licenciada'
    else:
        dic[lista_claves[3]]='Licenciado'
    if lista_contenido[6]=='f':
        dic[lista_claves[12]]='Coordinadora'
    else:
        dic[lista_claves[12]]='Coordinador'
    if lista_contenido[6]=='f':
        dic[lista_claves[13]]='la Tutora'
    else:
        dic[lista_claves[13]]='el Tutor'
    return(dic)
#
ejemplo_contenido=lee_pendientes('lista_veredictos.csv')[1]
#
nombre_especifico=diccionario(nombre_generico,ejemplo_contenido)
#
a = zipfile.ZipFile('test/plantilla_veredicto.odt')
content = a.read('content.xml')
content = str(content.decode(encoding='utf8'))
for i in nombre_generico:
    print(i,nombre_especifico[i])
    content = str.replace(content,i, nombre_especifico[i])
content = content.encode(encoding='utf8') #https://www.journaldev.com/23617/python-string-encode-decode
updateZip('test/prueba.odt', 'content.xml', content)
