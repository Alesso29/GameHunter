import pymongo
from pymongo import MongoClient
from pprint import pprint


tags = [
    "Horror psicologico",
    "Supervivencia",
    "Ambiente Opresivo",
    "Misterio Militar",
    "Zombis",
    "Combate Frenético",
    "Cooperacion",
    "Defensa",
    "Exploracion",
    "Sobrenatural",
    "Misterio",
    "Atmosfera inquietante",
    "Escape room",
    "Atmosfera angustiante",
    "Sobrevivencia",
    "Misterio Hospitalario",
    "Horror cómico",
    "Multijugador",
    "Ambiente infernal",
    "cazavampiros",
    "Acción frenética",
    "Combate siniestro",
    "Combate militar",
    "misiones tácticas",
    "Historia realista",
    "Operaciones especiales",
    "Objetos ocultos",
    "Ambiente oscuro",
    "Historia inquietante",
    "Acción explosiva",
    "historia intensa",
    "Combate contra narcos",
    "Historia histórica",
    "Estrategia militar",
    "Atmosfera ominosa",
    "Conquistas épicas",
    "Aventura de acción",
    "Mundo Abierto",
    "Simulador espacial",
    "Action-RPG",
    "Tipo GTA",
    "RPG Occidental",
    "Shooter en primera persona",
    "Hack and Slash",
    "Tipo Souls",
    "Survival Horror",
    "Metroidvania",
    "Sigilo",
    "Futbol",
    "Realismo",
    "Jugabilidad mejorada",
    "Modos de juego variados",
    "Jugabilidad realista",
    "Licencias de equipos",
    "Baloncesto",
    "Estrellas de la NBA",
    "Competicion en línea",
    "Lucha Libre",
    "Estrellas de la WWE",
    "Accion intensa",
    "Elementos RPG",
    "Equipo de jugadores",
    "Accion en el campo",
    "Tenis",
    "Jugabilidad autentica",
    "Jugadores reales",
    "Baile",
    "Canciones populares",
    "Diversion en movimiento",
    "Skateboarding",
    "Nostalgia",
    "Trucos",
    "Remasterizacion",
    "Beisbol",
    "Jugadores de la MLB",
    "Autenticidad",
    "Batallas Freneticas",
    "Animado",
    "Juego de Cartas",
    "Defensa de Torres",
    "Batallas epicas",
    "Imperios",
    "Fantasia/Magia",
    "Control del Mundo",
    "Misiones",
    "Oscuro Secreto",
    "Historia",
    "Avatar",
    "Animacion",
    "Universo",
    "Habilidades",
    "Nave espacial",
    "Cooperativo",
    "Historia Rica",
    "Exploracion",
    "Personalizacion",
    "Combate",
    "Equipo de Superheroes",
    "Historia epica",
    "Habilidades únicas",
    "Construccion creativa",
    "Aventura cooperativa",
    "Mundos generados",
    "Gestion de recursos",
    "Puzzles",
    "Batallas tácticas",
    "Personajes memorables",
    "Experiencia visual",
    "Conduccion libre",
    "Eventos emocionantes",
    "Variedad de vehículos",
    "Competición",
    "Conduccion extrema",
    "Gestion de terrenos",
    "Misiones desafiantes",
    "Personajes icónicos",
    "Power-ups",
    "Persecusiones policiales",
    "Competicion Nocturna",
    "Carreas ilegales",
    "Persecuciones intensas",
    "Destruccion de vehículos",
    "Combate en la pista",
    "Circuitos únicos",
    "Carreras callejeras",
    "Personalizacion extensa",
    "Exploracion urbana",
    "Realismo",
    "Variedad de autos",
    "Circuitos detallados",
    "Competicion en linea",
    "Acrobacias",
    "Desafios",
    "Dificultad creciente",
    "Exploracion submarina",
    "Mundos submarinos",
    "Crafteo",
    "Mechs personalizables",
    "Combate tactico",
    "Historia envolvente",
    "Personalizacion de armas",
    "Gestion de isla",
    "Interaccion social",
    "Actividades relajantes",
    "Captura de monstruos",
    "Mundo de fantasia",
    "Evolucion",
    "Granja",
    "Vida rural",
    "Combate aéreo",
    "Aviones personalizables",
    "Narrativa compleja",
    "Personajes multiples",
    "Elementos de Ciencia ficción",
    "Exploracion aérea",
    "Aviones detallados",
    "Construccion espacial",
    "Ingenieria",
    "Gestion de reino",
    "Estrategia",
    "Cooperacion local"
]

generos = [
    "terror",
    "accion",
    "aventura",
    "deportes",
    "estrategia",
    "carreras",
    "simulacion"
]


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


def imprimir_Respuestas2(respuestas_preguntas, usuario_pregunta):
    for pregunta_obj in respuestas_preguntas:
        if isinstance(pregunta_obj["pregunta"], str):
            if pregunta_obj["pregunta"] in usuario_pregunta:
                return pregunta_obj["respuesta"], pregunta_obj["pregunta"]

        elif isinstance(pregunta_obj["pregunta"], list):
            if all(palabra in usuario_pregunta for palabra in pregunta_obj["pregunta"]):
                return pregunta_obj["respuesta"], pregunta_obj["pregunta"]

    return None


def Conectar_Con_Mongo(Coleccion):
    uri = "mongodb+srv://Alesso:1234@alessoqueso.xnhdqly.mongodb.net/"

    client = MongoClient(uri)

    db = client['GameHunter']
    collection = db[Coleccion]
    return collection


def imprimir_Juego_Final(elemento_buscado):
    listatemp = []
    respuestaFinal = "El juego que te recomiendo es: "
    for clave, valor in elemento_buscado.items():
        listatemp.append(f"{clave}: {valor}")
    respuestaFinal += " ".join(listatemp)
    return respuestaFinal
