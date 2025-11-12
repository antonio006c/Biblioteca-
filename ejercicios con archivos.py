# Aprendiendo a trabajar con archivos de texto en python 

import json
import csv

# datos que quiero guardar en mi archivo json

datos = {
    "Nombre": "Antonio Cañete",
    "Edad": 33,
    "pais": "chile",
    "habilidades": ["Electrónica", "soporte técnico", "programación"],
    "trabajo remoto": True
}

with open ("datos.json", "w", encoding= "utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=4)    

print("Archivo 'datos.json' creado correctamente ✅")

# datos para guardar en archivo csv 

personas = [
    {"nombre" : "Antonio", "pais" : "chile", "edad": 33},
    {"nombre" : "alejandro", "pais" : "bolivia", "edad": 38},
    {"nombre" : "francisco", "pais" : "ecuador", "edad": 36},
]

with open ("personas.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "edad", "pais"] #encabezados
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader () #escribe la primera fila (encabezados)
    escritor.writerows(personas) #escribe todas las filas

print("Archivo 'personas.csv' creado correctamente ✅")


