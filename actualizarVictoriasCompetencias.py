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

def actualizar_victorias_en_competencias(alumno_id, competencia_id, nuevo_resultado):
    query = {
        "_id": alumno_id,
        "competencias.competencia_id": competencia_id
    }
    update = {
        "$set": {
            "competencias.$.resultado": nuevo_resultado
        }
    }
    
    result = collection_alumnos.update_one(query, update)
    if result.matched_count == 0:
        return f"No existe una competencia con ID {competencia_id} para el alumno con ID {alumno_id}"
    elif result.modified_count == 0:
        return f"No se ha modificado ninguna información para la competencia con ID {competencia_id} del alumno con ID {alumno_id}"


# Ejemplo de uso
alumno_id = 15
competencia_id = 1
nuevo_resultado = 2

mensaje = actualizar_victorias_en_competencias(alumno_id, competencia_id, nuevo_resultado)
print(mensaje)
