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

def borrar_alumno(alumno_id):
    query = {"_id": alumno_id}
    
    result = collection_alumnos.delete_one(query)
    if result.deleted_count == 0:
        return f"No existe un alumno con ID {alumno_id}"
    else:
        return f"Alumno con ID {alumno_id} ha sido borrado"

# Ejemplo de uso
alumno_id = 8

mensaje = borrar_alumno(alumno_id)
print(mensaje)
