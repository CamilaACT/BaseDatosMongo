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

def consulta_perfil_profesor_por_nombre(nombre):
    query = {"nombre": nombre}
    profesor = collection_usuarios.find_one(query)
    if profesor is None:
        return f"No se encontró un profesor con el nombre {nombre}"
    else:
        return profesor

# Ejemplo de uso
nombre_profesor = "María López"
perfil_profesor = consulta_perfil_profesor_por_nombre(nombre_profesor)
print(perfil_profesor)
