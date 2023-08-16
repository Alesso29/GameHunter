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


def imprimir_Respuestas(respuestas_preguntas, usuario_pregunta):

    respuesta_valida = False
    for pregunta_obj in respuestas_preguntas:
        if isinstance(pregunta_obj["pregunta"], str):
            if pregunta_obj["pregunta"] in usuario_pregunta:
                print(pregunta_obj["respuesta"])
                respuesta_valida = True
                return pregunta_obj["pregunta"]

        elif isinstance(pregunta_obj["pregunta"], list):
            if all(palabra in usuario_pregunta for palabra in pregunta_obj["pregunta"]):
                print(pregunta_obj["respuesta"])
                respuesta_valida = True
                return pregunta_obj["pregunta"]

    if not respuesta_valida:
        print("Lo siento, como un modelo muy simple de IA, no puedo contestar a esta pregunta :c .")
        return None


def buscar_genero(genero):
    collection = db['Game']
    if genero == "terror":
        filtro = {"name": "BATS: Bloodsucker Anti-Terror Squad"}
        documento = collection.find_one(filtro)
        if documento:
            pprint(documento)
        else:
            print("El documento no fue encontrado.")
    elif genero == "accion":

        collection = db['Game']
        return collection.find()


def imprimir_Respuestas2(respuestas_preguntas, usuario_pregunta):
    for pregunta_obj in respuestas_preguntas:
        if isinstance(pregunta_obj["pregunta"], str):
            if pregunta_obj["pregunta"] in usuario_pregunta:
                return pregunta_obj["respuesta"]

        elif isinstance(pregunta_obj["pregunta"], list):
            if all(palabra in usuario_pregunta for palabra in pregunta_obj["pregunta"]):
                return pregunta_obj["respuesta"]

    return None
