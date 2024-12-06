while True:  # Bucle para repetir el cálculo si el usuario lo desea
    # Solicitar datos al usuario
    precio = float(input("Ingresa el precio original del producto: "))
    descuento = float(input("Ingresa el porcentaje de descuento (sin %): "))

    # Validar que el precio y el descuento sean positivos
    if precio > 0 and descuento > 0:
        # Calcular el monto del descuento
        monto_descuento = precio * (descuento / 100)
        
        # Calcular el precio final
        precio_final = precio - monto_descuento
        
        # Mostrar los resultados
        print(f"\nEl monto del descuento es: ${monto_descuento:.2f}")
        print(f"El precio final con descuento es: ${precio_final:.2f}\n")
    else:
        print("\nEl precio y el porcentaje de descuento deben ser valores positivos.\n")

    # Preguntar si el usuario quiere calcular nuevamente
    continuar = input("¿Quieres calcular otro descuento, Pobreton? (s/n): ").lower()
    if continuar != 's':
        print("¡Gracias por usar el programa y dejar de buscar Descuentos Maldito Tacaño! 😊")
        break  # Salir del bucle si el usuario no desea continuar
