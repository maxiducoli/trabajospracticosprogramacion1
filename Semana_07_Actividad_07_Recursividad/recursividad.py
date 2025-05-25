# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


# def calcular_factorial_recursividad(num):
#     if num == 0 :
#         return 1
#     else:
#         return num * calcular_factorial_recursividad(num -1)


# def factorial_enteros(numero):

#     for x in range(1,numero + 1): # 1,2,3,4,5
#         print(f"El factorial de: {x} es {calcular_factorial_recursividad(x)}")

#numero = int(input("Ingrese un número entero: "))

# factorial_enteros(numero)




# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

# def Fibonaci(numero):
#     if numero == 0:
#         return 0
#     elif numero == 1:
#         return 1
#     else:
#         return Fibonaci(numero - 1 ) + Fibonaci(numero - 2)

# def Serie_Completa(numero):
#     for x in range(0,numero + 1):
#         print(f"Posición: {x} Valor: {Fibonaci(x)}")
# numero = int(input("Ingrese un número entero: "))

# Serie_Completa(numero)


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1).
# Prueba esta función en un algoritmo general. 

# def Potencia_recursiva(n,m):
#     # n = BASE
#     # m = EXPONENTE
#     if m == 0:
#         return 1
#     else:
#         return  n * Potencia_recursiva(n,m - 1) 

# #DEVUELVE => 2 * (2 * 3 - 1)
# #DEVULEVE => 2 * 2 * (2 * 2 - 1)
# #DEVULEVE => 2 * 2 * 2* (2 * 2 - 1)


# print(Potencia_recursiva(5,3))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto. 

# def Representacion_Binaria(numero):
    
#     if numero == 0:
#         return '0'
#     elif numero == 1:
#         return '1'
#     else:
#         return Representacion_Binaria(numero// 2) + str(numero % 2)
   
# print(Representacion_Binaria(13))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.      
# Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed(). 

# def es_palindromo(palabra):
#        if len(palabra) == 1:
#            return True
#        if palabra[0] != palabra[len(palabra)- 1]:
#            return False
#        return es_palindromo(palabra[1:-1])

# print(es_palindromo("neuquen"))

# 6) escribí una función recursiva en python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# # restricciones:
# # no se puede convertir el número a string.
# # usá operaciones matemáticas (%, //) y recursión.
# # ejemplos:
# # suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# # suma_digitos(9) → 9
# # suma_digitos(305) → 8 (3 + 0 + 5)

# def suma_digitos(n):
#      if n == 0:
#          return 0
#      else:
#          m = n % 10
#          return m + (suma_digitos(n // 10))

# print(suma_digitos(555))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# def contar_bloques(n):
#     if n == 0:
#         return 0
#     else:
#         return n + contar_bloques(n - 1)
        
# print(contar_bloques(4))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.       
# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0

# contador=0
# def contar_digito(numero, digito):
#     if numero == 0:
#         global contador
#         return contador
#     m = numero % 10                          
#     if m == digito:
#       contador+=1 
#     return contar_digito(numero // 10, digito)

# print(contar_digito(88881123324584470258881321,8))