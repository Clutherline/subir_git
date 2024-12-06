import string
import secrets

# Función para generar una contraseña segura
def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    # Definir los caracteres que pueden ser utilizados
    mayusculas = string.ascii_uppercase if incluir_mayusculas else ""
    minusculas = string.ascii_lowercase if incluir_minusculas else ""
    numeros = string.digits if incluir_numeros else ""
    simbolos = string.punctuation if incluir_simbolos else ""

    # Si no se selecciona ningún tipo de caracter, se genera una contraseña vacía
    todos_los_caracteres = mayusculas + minusculas + numeros + simbolos
    if not todos_los_caracteres:
        raise ValueError("Debe incluir al menos un tipo de carácter (mayúsculas, minúsculas, números, símbolos)")

    # Asegurarse de que la contraseña tenga al menos una de cada categoría
    contraseña = [
        secrets.choice(mayusculas) if incluir_mayusculas else "",
        secrets.choice(minusculas) if incluir_minusculas else "",
        secrets.choice(numeros) if incluir_numeros else "",
        secrets.choice(simbolos) if incluir_simbolos else ""
    ]
    
    # Completar la contraseña con caracteres aleatorios
    while len(contraseña) < longitud:
        contraseña.append(secrets.choice(todos_los_caracteres))
    
    # Mezclar los caracteres para que no estén organizados de manera predecible
    secrets.SystemRandom().shuffle(contraseña)
    
    # Convertir la lista de caracteres a una cadena
    return "".join(contraseña)

# Solicitar la longitud de la contraseña al usuario
longitud = int(input("Introduce la longitud deseada para la contraseña: "))

# Llamar a la función para generar la contraseña
contraseña_generada = generar_contraseña(longitud)

# Mostrar la contraseña generada
print("Contraseña generada:", contraseña_generada)
