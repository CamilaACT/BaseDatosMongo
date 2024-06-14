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


def informe_victorias_por_competencia(competencia_id):
    competencia = collection_competencias.find_one({"_id": competencia_id, "alumnos.resultado": 1}, {"alumnos.$": 1})
    return competencia

# Ejemplo de uso
competencia_id = 1
print(informe_victorias_por_competencia(competencia_id))
