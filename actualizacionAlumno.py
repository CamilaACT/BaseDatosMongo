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

def actualizar_informacion_alumno(alumno_id, nueva_informacion):
    query = {"_id": alumno_id}
    update = {"$set": nueva_informacion}
    
    result = collection_alumnos.update_one(query, update)
    if result.matched_count == 0:
        return f"No existe un alumno con ID {alumno_id}"
    elif result.modified_count == 0:
        return f"No se ha modificado ninguna información para el alumno con ID {alumno_id}"
    else:
        return f"Alumno con ID {alumno_id} ha sido actualizado"

# Ejemplo de uso
alumno_id = 1
nueva_informacion = {
    "nombre": "Juan Pérez Actualizado",
    "peso": 75,
    "altura": 178,
    "correo": "juan.perez.actualizado@example.com"
}

mensaje = actualizar_informacion_alumno(alumno_id, nueva_informacion)
print(mensaje)
