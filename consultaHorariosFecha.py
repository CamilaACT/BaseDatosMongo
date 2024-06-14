
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


def consulta_horarios_clase_por_fecha(fecha):
    pipeline = [
        {"$unwind": "$registros"},
        {"$match": {"registros.fecha": fecha}},
        {"$project": {
            "clase_id": "$_id",
            "tipo": 1,
            "subtipo": 1,
            "horario": 1,
            "fecha": "$registros.fecha"
        }}
    ]
    
    resultado = collection_clases.aggregate(pipeline)
    return list(resultado)

# Ejemplo de uso
fecha = datetime(2024, 6, 12, 11, 53, 3, 81000)
print(consulta_horarios_clase_por_fecha(fecha))
