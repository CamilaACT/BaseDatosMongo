from pymongo import MongoClient, errors

try:
    client = MongoClient('localhost', 27017)
    client.admin.command('ping')
    db = client.SatoriBD
    collection = db.Alumnos
    print("Conexión exitosa a MongoDB")
    alumnos = collection.find() 
    for alumno in alumnos:
        print(alumno)
except errors.ServerSelectionTimeoutError as err:
    print(f"Error de conexión: {err}")

except Exception as e:
    print(f"Error inesperado: {e}")
    