import secrets


# Caracteres que queremos incluir
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "@#$%&*"

# Todos los caracteres combinados
todos_los_caracteres = mayusculas + minusculas + numeros + simbolos

# Longitud de la contraseña
longitud = 12

# Generar la contraseña
contraseña = "".join(secrets.choice(todos_los_caracteres) for _ in range(longitud))

# Mostrar la contraseña generada
print("Contraseña generada:", contraseña)
