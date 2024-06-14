from pymongo import MongoClient, errors
from datetime import datetime

try:
    # Conectar a MongoDB en localhost en el puerto 27017
    client = MongoClient('localhost', 27017)

    # Intentar obtener el estado del servidor para verificar la conexión
    client.admin.command('ping')

    # Seleccionar la base de datos
    db = client.SatoriBD

    # Insertar documentos en la colección Cinturones
    collection_cinturones = db.Cinturones
    documentos_cinturones = [
        {
            "_id": 1,
            "nombre": "Cinturón Negro",
            "nivel": 5,
            "descripcion": "Máximo nivel",
            "fecha_creacion": datetime.now()
        },
        {
            "_id": 2,
            "nombre": "Cinturón Marrón",
            "nivel": 4,
            "descripcion": "Nivel avanzado",
            "fecha_creacion": datetime.now()
        },
        {
            "_id": 3,
            "nombre": "Cinturón Azul",
            "nivel": 3,
            "descripcion": "Nivel intermedio",
            "fecha_creacion": datetime.now()
        }
    ]
    result_cinturones = collection_cinturones.insert_many(documentos_cinturones)
    print(f'Documentos Cinturones insertados con los ids {result_cinturones.inserted_ids}')

    # Insertar documentos en la colección Alumnos
    collection_alumnos = db.Alumnos
    documentos_alumnos = [
        {
            "_id": 1,
            "nombre": "Juan Pérez",
            "peso": 70,
            "fecha_nacimiento": datetime(1990, 1, 1),
            "altura": 175,
            "correo": "juan.perez@example.com",
            "telefono": "123456789",
            "cedula": "12345678",
            "categorias": [
                {
                    "categoria_id": 1,
                    "fecha": datetime.now(),
                    "status": 1
                }
            ],
            "cinturones": [
                {
                    "cinturon_id": 1,
                    "fecha": datetime.now(),
                    "status": 1,
                    "puntuacion": 100
                }
            ],
            "competencias": [
                {
                    "competencia_id": 1,
                    "fecha": datetime.now(),
                    "tipo": 1,
                    "resultado": 1
                }
            ],
            "mensualidades": [
                {
                    "fecha": datetime.now(),
                    "monto": 50,
                    "status": 1
                }
            ],
            "asistencias": [
                {
                    "clase_id": 1,
                    "fecha": datetime.now()
                }
            ]
        },
        {
            "_id": 2,
            "nombre": "Ana García",
            "peso": 60,
            "fecha_nacimiento": datetime(1992, 2, 2),
            "altura": 160,
            "correo": "ana.garcia@example.com",
            "telefono": "987654321",
            "cedula": "87654321",
            "categorias": [
                {
                    "categoria_id": 2,
                    "fecha": datetime.now(),
                    "status": 1
                }
            ],
            "cinturones": [
                {
                    "cinturon_id": 2,
                    "fecha": datetime.now(),
                    "status": 1,
                    "puntuacion": 90
                }
            ],
            "competencias": [
                {
                    "competencia_id": 2,
                    "fecha": datetime.now(),
                    "tipo": 2,
                    "resultado": 2
                }
            ],
            "mensualidades": [
                {
                    "fecha": datetime.now(),
                    "monto": 60,
                    "status": 1
                }
            ],
            "asistencias": [
                {
                    "clase_id": 2,
                    "fecha": datetime.now()
                }
            ]
        }
    ]
    result_alumnos = collection_alumnos.insert_many(documentos_alumnos)
    print(f'Documentos Alumnos insertados con los ids {result_alumnos.inserted_ids}')

    # Insertar documentos en la colección Usuarios
    collection_usuarios = db.Usuarios
    documentos_usuarios = [
        {
            "_id": 1,
            "nombre": "María López",
            "especialidad": "Karate",
            "correo": "maria.lopez@example.com",
            "telefono": "987654321",
            "login": "maria.lopez",
            "password": "securepassword",
            "tipo_usuario": {
                "tipo_usuario_id": 1,
                "nombre": "Administrador",
                "descripcion": "Usuario con acceso total",
                "fecha_creacion": datetime.now()
            }
        },
        {
            "_id": 2,
            "nombre": "Carlos Díaz",
            "especialidad": "Judo",
            "correo": "carlos.diaz@example.com",
            "telefono": "112233445",
            "login": "carlos.diaz",
            "password": "securepassword",
            "tipo_usuario": {
                "tipo_usuario_id": 2,
                "nombre": "Instructor",
                "descripcion": "Usuario con acceso limitado",
                "fecha_creacion": datetime.now()
            }
        }
    ]
    result_usuarios = collection_usuarios.insert_many(documentos_usuarios)
    print(f'Documentos Usuarios insertados con los ids {result_usuarios.inserted_ids}')

    # Insertar documentos en la colección Clases
    collection_clases = db.Clases
    documentos_clases = [
        {
            "_id": 1,
            "tipo": 1,
            "subtipo": 2,
            "horario": "Lunes y Miércoles 18:00-19:00",
            "profesores": [
                {
                    "usuario_id": 1,
                    "fecha": datetime.now()
                }
            ],
            "registros": [
                {
                    "usuario_id": 1,
                    "fecha": datetime.now(),
                    "tipo": 1
                }
            ],
            "asistencias": [
                {
                    "alumno_id": 1,
                    "fecha": datetime.now()
                }
            ]
        },
        {
            "_id": 2,
            "tipo": 2,
            "subtipo": 1,
            "horario": "Martes y Jueves 19:00-20:00",
            "profesores": [
                {
                    "usuario_id": 2,
                    "fecha": datetime.now()
                }
            ],
            "registros": [
                {
                    "usuario_id": 2,
                    "fecha": datetime.now(),
                    "tipo": 1
                }
            ],
            "asistencias": [
                {
                    "alumno_id": 2,
                    "fecha": datetime.now()
                }
            ]
        }
    ]
    result_clases = collection_clases.insert_many(documentos_clases)
    print(f'Documentos Clases insertados con los ids {result_clases.inserted_ids}')

    # Insertar documentos en la colección Competencias
    collection_competencias = db.Competencias
    documentos_competencias = [
        {
            "_id": 1,
            "usuario_id": 1,
            "tipo": 1,
            "fecha": datetime.now(),
            "cantidad_alumnos": 20,
            "alumnos": [
                {
                    "alumno_id": 1,
                    "resultado": 1
                }
            ]
        },
        {
            "_id": 2,
            "usuario_id": 2,
            "tipo": 2,
            "fecha": datetime.now(),
            "cantidad_alumnos": 15,
            "alumnos": [
                {
                    "alumno_id": 2,
                    "resultado": 2
                }
            ]
        }
    ]
    result_competencias = collection_competencias.insert_many(documentos_competencias)
    print(f'Documentos Competencias insertados con los ids {result_competencias.inserted_ids}')

except errors.ServerSelectionTimeoutError as err:
    print(f"Error de conexión: {err}")
except errors.ConnectionFailure as err:
    print(f"Fallo de conexión: {err}")
except Exception as e:
    print(f"Error inesperado: {e}")
