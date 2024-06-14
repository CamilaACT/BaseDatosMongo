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

def informe_cobro_mensualidades_por_alumno(alumno_id):
    alumno = collection_alumnos.find_one({"_id": alumno_id}, {"mensualidades": 1, "nombre": 1})
    if alumno is None:
        return f"No se encontró un alumno con el ID {alumno_id}"
    if "mensualidades" not in alumno or not alumno["mensualidades"]:
        return f"El alumno con ID {alumno_id} no tiene registros de mensualidades"
    return alumno

# Ejemplo de uso
alumno_id = 1
resultado = informe_cobro_mensualidades_por_alumno(alumno_id)
print(resultado)
