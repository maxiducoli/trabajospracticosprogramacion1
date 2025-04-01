#1) Escribir un programa que solicite la edad del usuario.
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = input("Ingrese su edad: ")
if edad.isnumeric():
    edad = int(edad)
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Por favor, ingrese un número válido para la edad.")

