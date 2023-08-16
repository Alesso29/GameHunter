from flask import Flask, render_template, request, jsonify
import json
from utils import imprimir_Respuestas2

app = Flask(__name__)

# Carga de datos desde archivos JSON (similares a lo que tenías en tu script original)
with open("preguntas.json", 'r') as archivo:
    respuestas_preguntas = json.load(archivo)

with open("terror.json", 'r') as archivo:
    terror_p_r = json.load(archivo)

with open("simulacion.json", 'r') as archivo:
    simulacion_p_r = json.load(archivo)

with open("estrategia.json", 'r') as archivo:
    estrategia_p_r = json.load(archivo)

# Definir ruta para la página de chatbot


@app.route('/')
def chatbot_page():
    return render_template('chatbot.html')

# Definir ruta para manejar las solicitudes POST del chatbot


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensaje_usuario = data.get('mensaje', '')

    respuesta_bot = ""

    usuario_pregunta = mensaje_usuario.lower().split()
    respuesta_bot = imprimir_Respuestas2(
        respuestas_preguntas, usuario_pregunta)

    if "encontrar" in usuario_pregunta and "juego" in usuario_pregunta:
        tags = []
        pregunta_usuario = mensaje_usuario.lower()

        if pregunta_usuario == "terror":
            respuesta_bot = "¿Qué tipo de juego de terror estás buscando?"
            tags = terror_p_r

        elif pregunta_usuario == "simulacion":
            respuesta_bot = "¿Qué tipo de juego de simulación estás buscando?"
            tags = simulacion_p_r

        elif pregunta_usuario == "estrategia":
            respuesta_bot = "¿Qué tipo de juego de estrategia estás buscando?"
            tags = estrategia_p_r

        else:
            respuesta_bot = "Disculpa, desconozco información acerca de ese tipo de juego"

        if respuesta_bot and tags:
            while True:
                pregunta_usuario = mensaje_usuario.lower()
                if pregunta_usuario == "salir":
                    break

                usuario_pre = pregunta_usuario.split()
                temp = imprimir_Respuestas2(tags, usuario_pre)
                if temp not in tags and temp is not None:
                    tags.append(temp)
                    respuesta_bot = temp["respuesta"]
                else:
                    break

    if not respuesta_bot:
        respuesta_bot = "No entendí tu pregunta o no tengo información al respecto"

    return jsonify({"respuesta": respuesta_bot})


if __name__ == "__main__":
    app.run(debug=True)
