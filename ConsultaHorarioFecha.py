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

def consulta_horarios_clase_por_fecha(fecha):
    pipeline = [
        {"$unwind": "$asistencias"},
        {"$match": {"asistencias.fecha": fecha}},
        {"$project": {
            "clase_id": "$_id",
            "tipo": 1,
            "subtipo": 1,
            "horario": 1,
            "fecha": "$asistencias.fecha"
        }}
    ]
    
    resultado = list(collection_clases.aggregate(pipeline))
    if not resultado:
        return f"No se encontraron clases en la fecha {fecha}"
    else:
        return resultado

# Ejemplo de uso
fecha = datetime(2024, 6, 12, 11, 53, 3, 81000)
resultado = consulta_horarios_clase_por_fecha(fecha)
print(resultado)
