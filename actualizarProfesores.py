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

def actualizar_informacion_profesor(profesor_id, nueva_informacion):
    query = {"_id": profesor_id}
    update = {"$set": nueva_informacion}
    
    result = collection_usuarios.update_one(query, update)
    if result.matched_count == 0:
        return f"No existe un profesor con ID {profesor_id}"
    elif result.modified_count == 0:
        return f"No se ha modificado ninguna información para el profesor con ID {profesor_id}"


# Ejemplo de uso
profesor_id = 28
nueva_informacion = {
    "nombre": "María López Actualizada",
    "especialidad": "Taekwondo",
    "correo": "maria.lopez.actualizada@example.com",
    "telefono": "987654321"
}

mensaje = actualizar_informacion_profesor(profesor_id, nueva_informacion)
print(mensaje)
