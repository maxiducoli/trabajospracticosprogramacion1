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

#2) Escribir un programa que solicite su nota al usuario.
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”;
# en caso contrario deberá mostrar el mensaje “Desaprobado”. 

nota = input("Ingrese su nota: ")
if nota.isnumeric():
    nota = int(nota)
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
else:
    print("Por favor, ingrese un número válido para la nota.")

#3) Escribir un programa que permita ingresar solo números pares.
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. 

numero = input("Ingrese un número: ")
if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
        

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla
# a cuál de las siguientes categorías pertenece: 
#   ● Niño/a: menor de 12 años. 
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#   ● Adulto/a: mayor o igual que 30 años. 

edad = input("Ingrese su edad: ")
if edad.isnumeric():
    edad = int(edad)
    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")
else:
    print("Por favor, ingrese un número válido para la edad.")
    

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada,
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string. 

password = input("Ingrese su contraseña: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

