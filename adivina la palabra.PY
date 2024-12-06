import random

# 1. Lista de palabras para adivinar
palabras = ["python", "gato", "computadora", "programacion", "teclado"]
palabra = random.choice(palabras)  # Elige una palabra al azar
intentos = 6  # Número máximo de intentos
letras_adivinadas = []  # Lista para almacenar las letras que el jugador adivina

# 2. Instrucciones del juego
print("¡Bienvenido al juego de Ahorcado!")
print("Adivina la palabra letra por letra.")

# 3. Ciclo principal del juego
while intentos > 0:
    # Mostrar el progreso al jugador (letras adivinadas y guiones)
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    print("\nPalabra: ", progreso)

    # 4. Verificar si el jugador ha ganado
    if "_" not in progreso:
        print("¡Felicidades! Has adivinado la palabra:", palabra)
        break

    # 5. Solicitar una letra al jugador
    intento = input("Adivina una letra: ").lower()

    # 6. Verificar si la letra ya fue ingresada
    if intento in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue

    # 7. Añadir la letra a la lista de letras adivinadas
    letras_adivinadas.append(intento)

    # 8. Verificar si la letra está en la palabra
    if intento in palabra:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        intentos -= 1
        print("Incorrecto. Te quedan", intentos, "intentos.")

# 9. Fin del juego
if intentos == 0:
    print("Lo siento, has perdido maldito inutil. La palabra era:", palabra)
