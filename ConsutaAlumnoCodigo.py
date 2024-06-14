
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
collection_usuarios=db.Usuarios


def consulta_alumnos_por_clase(clase_id):
    pipeline = [
        {"$match": {"_id": clase_id}},
        {"$unwind": "$asistencias"},
        {"$lookup": {
            "from": "Alumnos",
            "localField": "asistencias.alumno_id",
            "foreignField": "_id",
            "as": "alumno_info"
        }},
        {"$unwind": "$alumno_info"},
        {"$project": {
            "clase_id": "$_id",
            "alumno_id": "$alumno_info._id",
            "alumno_nombre": "$alumno_info.nombre",
            "fecha_asistencia": "$asistencias.fecha"
        }}
    ]
    
    resultado = collection_clases.aggregate(pipeline)
    return list(resultado)

# Ejemplo de uso
clase_id = 1
print(consulta_alumnos_por_clase(clase_id))
