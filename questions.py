import random

print("¡Bienvenido al Ahorcado!")
print()

#armamos un diccionario con las diferentes palabras agrupadas por categoria
categorias = {
    'programacion': ['python', 'funcion', 'bucle', 'variable'],
    'autos': ['ferrari', 'volvo', 'volkswagen', 'mercedes'],
    'animales': ['gato', 'pajaro', 'rinoceronte', 'ballena']
}

#al iniciar cada partida, le mostramos al usuario las categorias disponibles para permitir que elija una
print('Categorias disponibles:')
for cat in categorias:
    print('-', cat)

#le pedimos al usuario que elija una de las categorias disponibles
elegida = input('Elegi una categoria: ')
words = categorias[elegida]


#usamos la funcion random.sample() para mezclar una lista con las palabras de la categoria elegida y devolverla sin repetir elementos
words_random = random.sample(words, len(words))


#creamos un bucle for para poder jugar varias rondas seguidas
for word in words_random:
    guessed = []
    attempts = 6
    puntaje = 0

    print()
    print('Nueva ronda!')
    print()

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje = puntaje + 6       #si adivina la palabra, suma 6 puntos
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        #verifica que el usuario ingrese SOLO un caracter, y que el mismo sea una letra y no un simbolo
        if len(letter) != 1 or not letter.isalpha(): 
            print('Entrada no valida')
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntaje = puntaje - 1       #si ingresa una letra incorrecta, se le resta 1 punto
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0     #si pierde el juego, queda con 0 puntos

    print('Tu puntaje final es:', puntaje)      #al final del juego imprime el puntaje
