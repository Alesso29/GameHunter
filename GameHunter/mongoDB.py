import pymongo
from pymongo import MongoClient
from pprint import pprint

# URL de conexión a MongoDB Atlas
uri = "mongodb+srv://Alesso:1234@alessoqueso.xnhdqly.mongodb.net/"

# Crear una instancia del cliente de MongoDB
client = MongoClient(uri)

# Seleccionar la base de datos y la colección
db = client['GameHunter']
collection = db['Game']

# Realizar una consulta y procesar los documentos
res = collection.find()
for document in res:
    pprint(document)
