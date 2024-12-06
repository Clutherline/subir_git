while True:  # Bucle infinito para seguir verificando números
    # Solicitar un número al usuario
    numero = int(input("Ingresa un número entero: "))
    
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
    
    # Preguntar si el usuario desea verificar otro número
    continuar = input("¿Quieres verificar otro número o acaso te quieres ir? (s/n): ").lower()
    if continuar != 's':
        print("¡Gracias por nada Adios!!")
        break  # Salir del bucle si el usuario no quiere continuar

