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

def consulta_perfil_alumno_por_nombre(nombre):
    query = {"nombre": nombre}
    alumno = collection_alumnos.find_one(query)
    if alumno is None:
        return f"No se encontró un alumno con el nombre {nombre}"
    else:
        return alumno

# Ejemplo de uso
nombre_alumno = "Juan Pérez"
perfil_alumno = consulta_perfil_alumno_por_nombre(nombre_alumno)
print(perfil_alumno)
