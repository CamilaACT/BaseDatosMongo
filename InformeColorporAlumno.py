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

def informe_alumnos_por_color_cinturon(nombre_cinturon):
    pipeline = [
        {"$unwind": "$cinturones"},
        {"$lookup": {
            "from": "Cinturones",
            "localField": "cinturones.cinturon_id",
            "foreignField": "_id",
            "as": "cinturon_info"
        }},
        {"$unwind": "$cinturon_info"},
        {"$match": {"cinturon_info.nombre": nombre_cinturon}},
        {"$project": {
            "alumno_id": "$_id",
            "alumno_nombre": "$nombre",
            "cinturon_nombre": "$cinturon_info.nombre",
            "cinturon_nivel": "$cinturon_info.nivel",
            "fecha": "$cinturones.fecha",
            "puntuacion": "$cinturones.puntuacion",
            "status": "$cinturones.status"
        }}
    ]
    
    resultado = collection_alumnos.aggregate(pipeline)
    return list(resultado)

# Ejemplo de uso
nombre_cinturon = "Cinturón Negro"
print(informe_alumnos_por_color_cinturon(nombre_cinturon))
