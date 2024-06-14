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
collection_mensualidades = db.Alumnos  # Las mensualidades están dentro de la colección Alumnos

def informe_asistencia_por_alumno(alumno_id):
    asistencias = collection_clases.aggregate([
        {"$unwind": "$asistencias"},
        {"$match": {"asistencias.alumno_id": alumno_id}},
        {"$project": {
            "fecha": "$asistencias.fecha",
            "clase_id": "$_id"
        }}
    ])
    resultado = list(asistencias)
    if not resultado:
        return f"No se encontraron asistencias para el alumno con ID {alumno_id}"
    else:
        return resultado

# Ejemplo de uso
alumno_id = 45
resultado = informe_asistencia_por_alumno(alumno_id)
print(resultado)
