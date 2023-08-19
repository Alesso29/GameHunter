# -⁻- coding: UTF-8 -*-
from flask import Flask, render_template, request, jsonify
import json
from utils import imprimir_Respuestas2
from utils import tags
from utils import generos
from utils import Conectar_Con_Mongo
from utils import imprimir_Juego_Final

app = Flask(__name__)
tags_aBuscar = []
GeneroSeleccionado = ""

with open("preguntas.json", 'r') as archivo:
    respuestas_preguntas = json.load(archivo)


@app.route('/')
def chatbot_page():
    return render_template('chatbot.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensaje_usuario = data.get('mensaje', '')

    respuesta_bot = ""
    pregunta = []

    usuario_pregunta = mensaje_usuario.lower().split()
    respuesta_bot, pregunta = imprimir_Respuestas2(
        respuestas_preguntas, usuario_pregunta)

    cadena_unida = " ".join(pregunta)

    if cadena_unida in tags:
        tags_aBuscar.append(cadena_unida)

    for palabra in usuario_pregunta:
        if palabra in generos:
            GeneroSeleccionado = palabra

    if len(tags_aBuscar) == 4:
        collection = Conectar_Con_Mongo(GeneroSeleccionado)
        elemento_buscado = collection.find_one({"tags": {"$in": tags_aBuscar}})
        jsonify({"respuesta": "Encontre tu juego ideal!!!"})
        respuesta_bot = imprimir_Juego_Final(elemento_buscado)

    if respuesta_bot == "Entendido reiniciare la busqueda":
        tags_aBuscar.clear()

    if not respuesta_bot:
        respuesta_bot = "No entendí tu pregunta o no tengo información al respecto"

    return jsonify({"respuesta": respuesta_bot})


if __name__ == "__main__":
    app.run(debug=True)
