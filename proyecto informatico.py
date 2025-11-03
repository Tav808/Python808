import random

def Adivina_el_Numero():
    print("\nADIVINA EL NÚMERO")
    print("\nElige el nivel de dificultad:")
    print("1. Fácil (1-50, 10 intentos)")
    print("2. Normal (1-100, 7 intentos)")
    print("3. Difícil (1-1000, 12 intentos)")
    
    dificultad = input("\nSelecciona 1, 2 o 3: ")
    
    if dificultad == '1':
        rango_min, rango_max = 1, 50
        intentos_maximos = 10
        nivel = "Fácil"
    elif dificultad == '2':
        rango_min, rango_max = 1, 100
        intentos_maximos = 7
        nivel = "Normal"
    elif dificultad == '3':
        rango_min, rango_max = 1, 1000
        intentos_maximos = 12
        nivel = "Difícil"
    else:
        print("Opción no válida. Se seleccionará Normal por defecto.")
        rango_min, rango_max = 1, 100
        intentos_maximos = 7
        nivel = "Normal"
    
    numero_secreto = random.randint(rango_min, rango_max)
    intentos = 0
    adivinado = False
    
    print(f"\nBienvenido al juego! Nivel: {nivel}")
    print(f"Deberás adivinar el número entre {rango_min} y {rango_max}.")
    print(f"Tienes {intentos_maximos} intentos.\n")
    
    while not adivinado and intentos < intentos_maximos:
        intento = input(f"Intento {intentos + 1 }/{intentos_maximos} - Introduce tu número: ")
        if not intento.isdigit():
            print("Por favor, introduce un número válido.")
            continue

        intento = int(intento)
        intentos += 1
        
        if intento < rango_min or intento > rango_max:
            print(f"Por favor, introduce un número entre {rango_min} y {rango_max}.")
            intentos -= 1
            continue
        
        if intento < numero_secreto:
            print("¡Más alto!")
        elif intento > numero_secreto:
            print("¡Más bajo!")
        else:
            adivinado = True
            print(f"\n¡Ganaste! El número era {numero_secreto}")
            print(f"En {intentos} intentos.")

    if not adivinado:
        print(f"\nTe quedaste sin intentos! El número era {numero_secreto}")
    
    print("\n¿Deseas seguir jugando o ir al menú?")
    continuar = input("Introduce 'jugar' para seguir jugando o 'menu' para ir al menú: ")
    if continuar.lower() == 'jugar':
        Adivina_el_Numero()
    elif continuar.lower() == 'menu':
        Menu()
    else:
        print("Opción no válida.")
        Menu()


def Juego_de_Preguntas():
    categorias = {
        "Ciencia": [
            {"pregunta": "¿Cuál es el planeta más grande del sistema solar?",
             "opciones": ["A) Marte", "B) Júpiter", "C) Saturno", "D) Neptuno"],
             "respuesta": "B"},
            {"pregunta": "¿Cuántos huesos tiene el cuerpo humano adulto?",
             "opciones": ["A) 206", "B) 198", "C) 215", "D) 187"],
             "respuesta": "A"},
            {"pregunta": "¿Qué son los humanos?",
             "opciones": ["A) Herbívoros", "B) Carnívoros", "C) Omnívoros", "D) Insectívoros"],
             "respuesta": "C"},
            {"pregunta": "¿Cuántas patas tiene una araña?",
             "opciones": ["A) 6", "B) 8", "C) 10", "D) 12"],
             "respuesta": "B"}
        ],
        "Historia": [
            {"pregunta": "¿Cuándo terminó la Segunda Guerra Mundial?",
             "opciones": ["A) 1943", "B) 1944", "C) 1945", "D) 1946"],
             "respuesta": "C"},
            {"pregunta": "¿Quién descubrió América?",
             "opciones": ["A) Américo Vespucio", "B) Cristóbal Colón", "C) Fernando de Magallanes", "D) Hernán Cortés"],
             "respuesta": "B"},
            {"pregunta": "¿En qué año cayó el Muro de Berlín?",
             "opciones": ["A) 1987", "B) 1988", "C) 1989", "D) 1990"],
             "respuesta": "C"}
        ],
        "Geografía": [
            {"pregunta": "¿Cuál es la capital de Francia?",
             "opciones": ["A) Londres", "B) Berlín", "C) Madrid", "D) París"],
             "respuesta": "D"},
            {"pregunta": "¿Cuál es el río más largo del mundo?",
             "opciones": ["A) Amazonas", "B) Nilo", "C) Yangtsé", "D) Misisipi"],
             "respuesta": "B"},
            {"pregunta": "¿Cuál es el país más grande del mundo?",
             "opciones": ["A) Canadá", "B) China", "C) Rusia", "D) Estados Unidos"],
             "respuesta": "C"},
            {"pregunta": "¿Cuál es el océano más grande del mundo?",
             "opciones": ["A) Atlántico", "B) Índico", "C) Ártico", "D) Pacífico"],
             "respuesta": "D"}
        ],
        "Cultura Pop": [
            {"pregunta": "¿Cuál es el animal más rápido del mundo?",
             "opciones": ["A) León", "B) Guepardo", "C) Águila", "D) Tiburón"],
             "respuesta": "B"},
            {"pregunta": "¿Qué pesa más?",
             "opciones": ["A) Un kilo de plumas", "B) Un kilo de plomo", "C) Pesan lo mismo", "D) Depende de la temperatura"],
             "respuesta": "C"},
            {"pregunta": "¿Cuántos minutos tiene un partido de fútbol?",
             "opciones": ["A) 80", "B) 90", "C) 100", "D) 120"],
             "respuesta": "B"}
        ]
    }
    
    print("\nJUEGO DE PREGUNTAS")
    print("\nSelecciona una categoría:")
    print("1. Ciencia")
    print("2. Historia")
    print("3. Geografía")
    print("4. Cultura Pop")
    print("5. Todas las categorías (mezcladas)")
    
    eleccion = input("\nElige una opción (1-5): ")
    
    if eleccion == '1':
        preguntas_seleccionadas = categorias["Ciencia"]
        categoria_nombre = "Ciencia"
    elif eleccion == '2':
        preguntas_seleccionadas = categorias["Historia"]
        categoria_nombre = "Historia"
    elif eleccion == '3':
        preguntas_seleccionadas = categorias["Geografía"]
        categoria_nombre = "Geografía"
    elif eleccion == '4':
        preguntas_seleccionadas = categorias["Cultura Pop"]
        categoria_nombre = "Cultura Pop"
    elif eleccion == '5':
        preguntas_seleccionadas = []
        for preguntas in categorias.values():
            preguntas_seleccionadas.extend(preguntas)
        random.shuffle(preguntas_seleccionadas)
        categoria_nombre = "Todas las categorías"
    else:
        print("Opción no válida. Se seleccionarán todas las categorías.")
        preguntas_seleccionadas = []
        for preguntas in categorias.values():
            preguntas_seleccionadas.extend(preguntas)
        random.shuffle(preguntas_seleccionadas)
        categoria_nombre = "Todas las categorías"
    
    puntaje = 0
    total_preguntas = len(preguntas_seleccionadas)
    
    print(f"\nBienvenido al juego de preguntas! Categoría: {categoria_nombre}")
    print(f"Responde {total_preguntas} preguntas\n")
    
    for i, item in enumerate(preguntas_seleccionadas, 1):
        print(f"\nPregunta {i}/{total_preguntas}")
        print(item["pregunta"])
        for opcion in item["opciones"]:
            print(opcion)
        
        respuesta_usuario = input("\nTu respuesta (A/B/C/D): ").strip().upper()
        
        if respuesta_usuario == item["respuesta"]:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {item['respuesta']}")
    
    print(f"\nPUNTAJE FINAL: {puntaje}/{total_preguntas}")
    porcentaje = (puntaje / total_preguntas) * 100
    print(f"Porcentaje de aciertos: {porcentaje:.1f}%")
    
    if porcentaje == 100:
        print("¡PERFECTO! ¡Eres un experto!")
    elif porcentaje >= 80:
        print("¡Excelente trabajo!")
    elif porcentaje >= 60:
        print("¡Buen trabajo!")
    elif porcentaje >= 40:
        print("¡Sigue practicando, vas bien!")
    else:
        print("¡No te rindas, la práctica hace al maestro!")
    
    continuar = input("¿Deseas volver al menú? (si/no): ")
    if continuar.lower() in ['si', 's', 'sí']:
        Menu()
    else:
        print("¡Gracias por jugar!")


def Menu():
    print("MENÚ PRINCIPAL DE JUEGOS")
    print("""
         _        _       _ _       _                    _ 
        / |      / \   __| (_)_   _(_)_ __   __ _    ___| |
        | |     / _ \ / _` | \ \ / / | '_ \ / _` |  / _ \ |
        | |_   / ___ \ (_| | |\ V /| | | | | (_| | |  __/ |
        |_(_) /_/  _\_\__,_|_| \_/_|_|_| |_|\__,_|  \___|_|
        | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \              
        | | | | |_| | | | | | |  __/ | | (_) |             
        |_| |_|\__,_|_| |_| |_|\___|_|  \___/              
        """)

    print("""
         ____          _                              _      
        |___ \        | |_   _  ___  __ _  ___     __| | ___ 
          __) |    _  | | | | |/ _ \/ _` |/ _ \   / _` |/ _ \\
         / __/ _  | |_| | |_| |  __/ (_| | (_) | | (_| |  __/
        |_____(_)  \___/ \__,_|\___|\__, |\___/   \__,_|\___|
        |  _ \ _ __ ___  __ _ _   _ |___/| |_ __ _ ___       
        | |_) | '__/ _ \/ _` | | | | '_ \| __/ _` / __|      
        |  __/| | |  __/ (_| | |_| | | | | || (_| \__ \\      
        |_|   |_|  \___|\__, |\__,_|_| |_|\__\__,_|___/      
                        |___/                                
        """)
        
    print("""
         _____    ____        _ _      
        |___ /   / ___|  __ _| (_)_ __ 
          |_ \   \___ \ / _` | | | '__|
         ___) |   ___) | (_| | | | |   
        |____(_) |____/ \__,_|_|_|_|   
        """)
    
    eleccion = input("\nElige el proyecto a ejecutar (1, 2 o 3): ")
    print()
    
    if eleccion == '1':
        Adivina_el_Numero()
    elif eleccion == '2':
        Juego_de_Preguntas()
    elif eleccion == '3':
        print("¡Gracias por jugar! ¡Hasta pronto!")
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        Menu()

Menu()
