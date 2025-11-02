"""Proyecto 8 “Adivina el Número”:

● La computadora elige un número al azar.
● El usuario intenta adivinarlo con pistas (“más alto” / “más bajo”).

● Contar intentos.

Proyecto 5 “Juego de Preguntas”:

● Usar una lista o diccionario con preguntas y respuestas.
● Contar cuántas acierta el jugador.
● Mostrar puntaje final.

Menu
    interactivo para elegir el proyecto a ejecutar."""

def Adivina_el_Numero():
    import random
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego!")
    print("Deberas adivinar el numero que he pensado, entre el 1 y el 100.")
    print("Tienes intentos ilimitados")
    print()
    print("¡Disfruta el juego!")
    print()

    while not adivinado:
        intento = int(input("Introduce tu numero: "))
        intentos += 1

        if intento < numero_secreto:
            print("Mas alto.")
        elif intento > numero_secreto:
            print("Mas bajo.")
        else:
            adivinado = True
            print("¡Felicidades adivinaste!, el numero era", numero_secreto, "y usaste", intentos, "intentos.")

    print("Desea seguir jugando o ir al menu?")
    continuar = input("Introduce 'jugar' para seguir jugando o 'menu' para ir al menu: ")
    if continuar.lower() == 'jugar':
        Adivina_el_Numero()
    elif continuar.lower() == 'menu':
        Menu()
    else:
        print("Opción no válida.")
        Menu()

def Juego_de_Preguntas():
    preguntas = {
        "¿Cuál es la capital de Francia?": "paris",
        "¿Cual es el planeta mas grande del sistema solar?": "jupiter",
        "¿Cual es el rio mas largo del mundo?": "nilo",
        "¿Cuantos huesos tiene el cuerpo humano?": "206",
        "¿Cual es el pais mas grande del mundo?": "rusia",
        "¿Cual es el oceano mas grande del mundo?": "pacifico",
        "¿Cuando termino la segunda guerra mundial?": "1945",
        "¿Que son los humanos, omnivoros, herbivoros o carnivoros?": "omnivoros",
        "¿Cuantas patas tiene una araña?": "8",
        "¿Cual es el animal mas rapido del mundo?": "guepardo",
        "¿Que pesa mas, un kilo de plumas o un kilo de plomo? (plumas, plomo o ninguno)": "ninguno"

    }

    puntaje = 0

    print("¡Bienvenido al juego de preguntas!")
    for pregunta, respuesta in preguntas.items():
        respuesta_usuario = input(pregunta + " ")
        if respuesta_usuario.lower() == respuesta.lower():
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto. La respuesta correcta es:", respuesta)

    print("Tu puntaje final es:", puntaje)

def Menu():
    print("1. Proyecto 8 “Adivina el Número”")
    print("2. Proyecto 5 “Juego de Preguntas”")
    eleccion = input("Elige el proyecto a ejecutar (1 o 2): ")
    print()
    if eleccion == '1':
        Adivina_el_Numero()
    elif eleccion == '2':
        Juego_de_Preguntas()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        Menu()


Menu()
