# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] += 130
precios_frutas["Manzana"] += 200
precios_frutas["Melón"] = 2800


#print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

def lista_frutas(precios_frutas):
    lista_frutas = []
    for fruta in precios_frutas:
        lista_frutas.append(fruta)
    return lista_frutas

#print(lista_frutas(precios_frutas))

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

def mini_agenda():
    contacto = {}
    for i in range(5):
        nombre = input("Por favor ingrese un nombre: ")
        contacto[nombre] = input("Por favor ingrese un número de teléfono: ")
    
    nombre_buscar = input("Ingrese el nombre a buscar: ")

    if  nombre_buscar in contacto:
            return contacto[nombre_buscar]
    else:
        return "El nombre no existe."

#print(mini_agenda())

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

def separa_palabras():
     frase = input("Ingrese una fase: ")
     return frase.split()

#frase = separa_palabras()
#print(set(frase))

def cuenta_palabras(palabras):
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra]  = 1
    return contador               

#print(cuenta_palabras(frase))

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

def calificaciones():
    alumnos = []
    califica = {}
    i = 0
    while i < 3:
        alumnos.append(input("Ingrese un alumno: "))
        i += 1
    for alumno in alumnos:
        notas = (
        int(input(f"ingrese la primer nota para {alumno}: ")),
        int(input(f"ingrese la segunda nota para {alumno}: ")),
        int(input(f"ingrese la tercer nota para {alumno}: "))
        )
        califica[alumno] =  notas
    return califica

def promedio(calificaciones):
    promedios = {}
    for alumno, calificacion in calificaciones.items():
        prom = sum(calificacion) / len(calificacion)
        promedios[alumno] = prom
    return promedios

#print(promedio(calificaciones()))

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Juan" : 10, "Sofía" : 8, "Julián" : 7, "Jorge" : 9}
parcial2 = {"Juan" : 10, "Sofía" : 7, "Julián" : 8, "Jorge" : 10}

def aprobadores(parcial1,parcial2):
    listado = {}
    for alumno  in parcial1:
        listado[alumno] = ""

    for alumno2 in parcial2:
        listado[alumno2] = ""

    return listado

#print(set(aprobadores(parcial1,parcial2)))


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {"Batata" : 500, "Remolacha" : 300, "Banana" : 200, "Manzana" : 300, "Peras" : 250, "Zanahoria" : 100, "Cebolla" : 150, "Rabanito" : 100, "Radicheta" : 220, "Pomelo" : 180}

def consultar_stock(producto):
    return productos.get(producto,"Producto no encontrado")

#print(consultar_stock("Manzana"))

def agregar_stock(producto,cantidad):
    if producto in productos:
        productos[producto] += cantidad
    return f"Se agregaron {cantidad} unidades de {producto} al stock y ahora es stock es de {productos[producto]}"

#print(agregar_stock("Manzana",50))

def actualizar_stock(producto,cantidad):
    if  producto not in productos:
        productos[producto] = cantidad
    return productos

#print(actualizar_stock("Moñato",500))

        
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# agenda = {("Lunes" , "10:00:00") : "Reunión",("Martes", "15:00:00") : "Clase de inglés"}
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {("Lunes" , "10:00:00") : "Reunión",
          ("Martes", "15:00:00") : "Clase de inglés",
          ("Miércoles", "13:00:00") : "Clase de Karate",
          ("Jueves", "05:00:00") : "Trotar"
          ,("Viernes", "11:00:00") : "Clase de dibujo"
          }

def consultar_agenda(dia_hora):
    if dia_hora in agenda:
        return agenda[dia_hora]
    else:
        return "Sin eventos"

#print(consultar_agenda(("Domingo","10:00:00")))


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
    
paises_y_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago de Chile",
    "Colombia": "Bogotá",
    "Costa Rica": "San José",
    "Cuba": "La Habana",
    "Ecuador": "Quito",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Japón": "Tokio",
    "México": "Ciudad de México",
    "Perú": "Lima",
    "Portugal": "Lisboa",
    "Reino Unido": "Londres",
    "Rusia": "Moscú",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas"
}

def invertir_claves(paises_y_capitales):
    nuevo_diccionario = {}
    for paises in paises_y_capitales:
        nuevo_diccionario[paises_y_capitales[paises]] = paises
    return nuevo_diccionario

print(invertir_claves(paises_y_capitales))