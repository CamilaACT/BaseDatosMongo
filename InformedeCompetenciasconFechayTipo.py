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


def informe_competencias(fecha, tipo):
    query = {"fecha": fecha, "tipo": tipo}
    
    competencias = collection_competencias.find(query)
    return list(competencias)

# Ejemplo de uso
fecha = datetime(2024, 6, 12, 11, 53, 3, 81000)
tipo = 1

# Buscar por fecha y tipo
print(informe_competencias(fecha, tipo))
# Las mensualidades están dentro de la colección Alumnos