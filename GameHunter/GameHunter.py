import json
from utils import imprimir_Respuestas

if __name__ == "__main__":

    with open("preguntas.json", 'r') as archivo:
        respuestas_preguntas = json.load(archivo)

    with open("terror.json", 'r') as archivo:
        terror_p_r = json.load(archivo)

    with open("simulacion.json", 'r') as archivo:
        simulacion_p_r = json.load(archivo)

    with open("estrategia.json", 'r') as archivo:
        estrategia_p_r = json.load(archivo)

    while True:
        print()
        pregunta_usuario = input("Usuario: ")
        usuario_pregunta = pregunta_usuario.lower().split()

        if pregunta_usuario.lower() == "salir":
            print("Hasta luego!!!!")
            break

        respuesta_valida = imprimir_Respuestas(
            respuestas_preguntas, usuario_pregunta)

        if "encontrar" in usuario_pregunta and "juego" in usuario_pregunta:
            print()
            tags = []
            pregunta_usuario = input("Usuario: ")

            if pregunta_usuario.lower() == "terror":
                print("¿Qué tipo de terror estás buscando?")
                while True:
                    print()
                    pregunta_usuario = input("Usuario: ")

                    if pregunta_usuario.lower() != "salir":
                        usuario_pre = pregunta_usuario.lower().split()
                        temp = imprimir_Respuestas(
                            terror_p_r, usuario_pre)
                        if temp not in tags and temp != None:
                            tags.append(temp)
                    else:
                        break

            elif pregunta_usuario.lower() == "simulacion":
                print("¿Qué tipo de simulacion estás buscando?")
                while True:
                    print()
                    pregunta_usuario = input("Usuario: ")

                    if pregunta_usuario.lower() != "salir":
                        usuario_pre = pregunta_usuario.lower().split()
                        temp = imprimir_Respuestas(
                            simulacion_p_r, usuario_pre)
                        if temp not in tags and temp != None:
                            tags.append(temp)
                    else:
                        break

            elif pregunta_usuario.lower() == "estrategia":
                print("¿Qué tipo de estrategia estás buscando?")
                while True:
                    print()
                    pregunta_usuario = input("Usuario: ")

                    if pregunta_usuario.lower() != "salir":
                        usuario_pre = pregunta_usuario.lower().split()
                        temp = imprimir_Respuestas(
                            estrategia_p_r, usuario_pre)
                        if temp not in tags and temp != None:
                            tags.append(temp)
                    else:
                        break

            else:
                print("Disculpa desconozco informacion acerca de ese juego")
