def calculadora():
    resultado = None
    while True:
        if resultado is None:
            # Primera operación, pedimos dos números
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
        else:
            # Después de la primera operación, usamos el resultado anterior
            print(f"\nResultado actual: {resultado}")
            num1 = resultado
            num2 = int(input("Ingresa otro número: "))
        
        # Pedimos la operación
        operacion = input("Elige una operación (+, -, *, /) o 'salir' para terminar: ")
        
        # Realizamos la operación
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("No se puede dividir entre cero.")
                continue
        elif operacion.lower() == "salir":
            print("BYE BYE INUTIL.")
            break
        else:
            print("Operación no válida.")
            continue
        
        print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()
