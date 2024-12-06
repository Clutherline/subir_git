# Solicitar los datos del usuario
peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))

# Calcular el IMC usando el operador de potencia
imc = peso / (altura ** 2)  # altura al cuadrado

# Mostrar el resultado
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Clasificar el resultado según el IMC
if imc < 18.5:
    print("Estás bajo de peso.")
elif 18.5 <= imc < 24.9:
    print("Tienes un peso normal.")
elif 25 <= imc < 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")
