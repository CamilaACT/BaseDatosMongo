from pymongo import MongoClient, errors
from datetime import datetime

# Conectar a MongoDB en localhost en el puerto 27017
client = MongoClient('localhost', 27017)
db = client.SatoriBD

# Seleccionar las colecciones
collection_alumnos = db.Alumnos
collection_clases = db.Clases
collection_competencias = db.Competencias
collection_cinturones = db.Cinturones
collection_mensualidades = db.Alumnos
collection_usuarios = db.Usuarios

def consulta_perfil_clase_por_codigo(clase_id):
    query = {"_id": clase_id}
    clase = collection_clases.find_one(query)
    if clase is None:
        return f"No se encontró una clase con el ID {clase_id}"
    else:
        return clase

# Ejemplo de uso
clase_id = 1
perfil_clase = consulta_perfil_clase_por_codigo(clase_id)
print(perfil_clase)
