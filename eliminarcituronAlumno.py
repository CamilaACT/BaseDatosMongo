
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


def eliminar_cinturon_de_alumno(alumno_id, cinturon_id):
    query = {"_id": alumno_id}
    update = {
        "$pull": {
            "cinturones": {"cinturon_id": cinturon_id}
        }
    }
    
    result = collection_alumnos.update_one(query, update)
    return result.modified_count

# Ejemplo de uso
alumno_id = 1
cinturon_id = 1

modificados = eliminar_cinturon_de_alumno(alumno_id, cinturon_id)
print(f'Documentos modificados: {modificados}')
