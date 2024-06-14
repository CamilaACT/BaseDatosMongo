
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

def borrar_profesor(profesor_id):
    query = {"_id": profesor_id}
    
    result = collection_usuarios.delete_one(query)
    return result.deleted_count

# Ejemplo de uso
profesor_id = 5

borrados = borrar_profesor(profesor_id)
print(f'Documentos borrados: {borrados}')








