calificacion1 = float(input("ingresa la calificacion de la primera materia:"))
calificacion2 = float(input("ingresa la calificacion de la segunda materia:"))
calificacion3 = float(input("ingresa la calificacion de la tercera materia:"))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3
if calificacion1 < 3 or calificacion2 < 3 or calificacion3 < 3:
  print("calificacion muy baja.")
else:
    if promedio >= 7:
        print("aprobado")
    elif promedio >= 5:
        print("recuperacion")
    else:
        print("reprobado")
        
