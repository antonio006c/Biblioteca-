# Aqui vamos a crear un archivo en una carpeta en mi escritorio

import os

#Esta función guarda el contenido de un archivo en una carpeta que ya existe en mi escritorio
def guardar_archivo_en_carpeta (nombre_archivo, nombre_carpeta, contenido):
    
    #1 obtener la ruta base del escritorio
    ruta_escritorio = os.path.join(os.path.expanduser('~')), 'Desktop'

    #2 construir la ruta completa a la carpeta de destino
    ruta_carpeta_destino = os.path.join(ruta_escritorio, nombre_carpeta)

    #3 construir la ruta completa del archivo
    ruta_completa_archivo = os.path.join(ruta_carpeta_destino, nombre_archivo)

    #verificar que la carpeta exista antes de intentar escribir
    if not os.path.isdir(ruta_carpeta_destino):
        print(f" ❌ La carpeta '{nombre_carpeta}' no existe en el escritorio ")
        print("Por favor crear carpeta o revisa ortigrafía")
        return

    try:
    #guardar archivo en la ruta completa
        with open(ruta_completa_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
        print("")
        

    except Exception as e:

