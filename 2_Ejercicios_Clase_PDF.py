from math import sqrt, floor
from math import pi

# #######################
# Ejercicio Pirámide
# #######################
# Dada una altura, pintar una pirámide como la siguiente:
#   *
#  ***
# *****

def piramide(altura):
    for i in range(altura):
        huecos = altura-(i+1)
        estrellas = (i*2)+1
        print(' '*huecos + '*'*estrellas)

def piramide_pro(altura):
    for i in range(altura):
        print(' '*(altura-(i+1)) + '*'*((i*2)+1))

def piramide_invertida(altura):
    for i in range(altura):
        huecos = i
        estrellas = (altura*2)-(i*2)-1
        print(' '*huecos + '*'*estrellas)

def piramide_invertida_pro(altura):
    for i in range(altura):
        print(' '*i + '*'*(altura*2-(i*2)-1))

def piramide_invertida_superpro(altura):
    for i in reversed(range(altura)):
        print(' '*(altura-(i+1)) + '*'*((i*2)+1))

# piramide(3)
# piramide_pro(3)
# piramide_invertida(3)
# piramide_invertida_pro(3)
# piramide_invertida_superpro(3)


# #######################
# Ejercicio Rombo
# #######################

def rombo(altura):
    for i in range(altura):
        print(' ' * (altura - (i + 1)) + '*' * ((i * 2) + 1))
    for j in reversed(range(altura-1)):
        print(' ' * (altura - (j + 1)) + '*' * ((j * 2) + 1))


def rombo_clase(altura):
    for i in range(altura):
        print(" " * (altura - i) + "*" * (2 * i + 1))
    for i in range(altura - 2, -1, -1):
        print(" " * (altura - i) + "*" * (2 * i + 1))

# rombo(3)
# rombo_clase(3)

# ###############################
# Ejercicios FUNCIONES (RANDOM) PDF
# ################################

# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el área de un rectángulo.
# ___________________________________________________________________________________________________________________
def area_triangulo(a,b):
    return a*b
# print(area_triangulo(2,4))


# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el perímetro de una circunferencia (utilizando math).
# ___________________________________________________________________________________________________________________
def perimetro_circunferencia(radio):
    return 2*pi*radio
# print(perimetro_circunferencia(5))


# ___________________________________________________________________________________________________________________
# Crear una función que resuelve una ecuación de segundo grado recibiendo a, b, c.
# ___________________________________________________________________________________________________________________
def ecuacion(a,b,c):
    sol = ((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    return (sol)
# print(ecuacion(1,3,2))


# ___________________________________________________________________________________________________________________
# Crear una función que calcule el factorial de n.
# ___________________________________________________________________________________________________________________
def factorial(n):
    fac = 1
    if n > 0:
        for i in range(n):
            fac = fac*(i+1)
    return fac

def factorial_recursivo(n):
    # Consume muchos recursos. No es recomendable.
    if n < 2:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def factorial_clase(n):
    f = 1
    for i in range(n + 1):
        if i != 0:
            f = f * i
        else:
            continue
    return f

# print(factorial(5))
# # print(factorial_recursivo(5))
# # print(factorial_clase(5))


# ___________________________________________________________________________________________________________________
# Crear una función que devuelva una lista con los números primos de 0 a 100.
# ___________________________________________________________________________________________________________________
def generar_primos_pro(limite):
    lst = [x for x in range(1, limite+1) if es_primo_pro(x)]  # CUIDADO CON RANGE. Si quieres que vaya de 1 a N,
                                                              # tienes que poner (1,N+1) para que te incluya N
    return lst
def es_primo_pro(num):
    for j in range(2, floor(sqrt(num))+1):
        # Con esto genero los divisores que han de ir de 2 a (raíz del número)+1 (para que lo coja el rango)
        if num % j == 0:
            return False
    return True

# print(es_primo_pro(25))  # False
# print(es_primo_pro(17))  # True
# print(es_primo_pro(44))  # False

# print(generar_primos_pro(101))

# Lo de clase:
def isprime(n, p):
    for e in p:
        if n % e == 0:
            return False;
    return True

def primos():
    p = set()
    for e in range(2, 100):
        if isprime(e, p):
            p.add(e)

    return p


# ___________________________________________________________________________________________________________________
#  Dada una lista, imprimir los elementos en posición par.
# ___________________________________________________________________________________________________________________
def imprimir_posicion_par(lista):
    for i, j in enumerate(lista):
        if i % 2 == 0:
            print(j)

# imprimir_posicion_par(['1','a','2','b','3','c','4','d'])   # Debe sacar los números


# ___________________________________________________________________________________________________________________
# Un número es perfecto si la suma de sus divisores es igual a si mismo, ejemplo el 28.
# Crear una función que devuelva si un número es perfecto.
# ___________________________________________________________________________________________________________________
def numero_perfecto(num):
    divisores = [x for x in range(1, floor(num / 2) + 1) if num % x == 0]
    return sum(divisores) == num

# print(numero_perfecto(28))
# print(numero_perfecto(496))
# print(numero_perfecto(8128))
# print(numero_perfecto(6))
# print(numero_perfecto(66))
# print(numero_perfecto(7))

def divisores(num):
    # x son los divisores de num. Tengo que generarlos desde 1,2,3... hasta la mitad del numero
    # y sólo se inlcuyen en la lista si el num es divisible por ellos
    divisores = [x for x in range(1, floor(num/2)+1) if num % x == 0]
    return divisores


# ___________________________________________________________________________________________________________________
# Crear una función que recibe una lista de números y devuelve una lista de tuplas por cada elemento.
# Cada tupla tendrá el elemento, su cuadrado y su cubo:
# ___________________________________________________________________________________________________________________
def elemento_cuadrado_cubo_pro(lista):
    return [(x, x**2, x**3) for x in lista]

# print(elemento_cuadrado_cubo_pro([1, 2, 3, 4, 5]))
# [(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]



# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el máximo y mínimo de 2 números.
# ___________________________________________________________________________________________________________________
def maxmin(a,b):
    return (a, b) if a > b else (b, a)

# print(maxmin(7, 8))
# print(maxmin(5, 3))


# ___________________________________________________________________________________________________________________
# Crear un función que devuelva el máximo y mínimo de una lista de números.
# ___________________________________________________________________________________________________________________
def max_y_min(lista):
    max = lista[0]
    min = lista[0]
    for i in lista:
        if max < i:
            max = i
        elif min > i:
            min = i
    return (max,min)

# mi_lista = [1, 12, 2, 53, 23, 6, 17]
# print(max_y_min(lista=mi_lista))

# ___________________________________________________________________________________________________________________
# Crea una función que recibe una cadena y la devuelve en sentido inverso
# ___________________________________________________________________________________________________________________
def reversed_string(cadena):
    return cadena[::-1]

# print(reversed_string('hola caracola'))

# ___________________________________________________________________________________________________________________
# Crea una función que recibe una cadena y devuelve la misma cadena con sólo la primera letra mayúscula.
# ___________________________________________________________________________________________________________________
def primera_mayuscula(cadena):
    return cadena[0].upper()+cadena[1:].lower()

# print(primera_mayuscula('la primEra con MaYUSCula'))

# ___________________________________________________________________________________________________________________
# Crea una función que imprima por pantalla una matriz (lista de listas).
# ___________________________________________________________________________________________________________________
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        fila = str()
        for j in range(len(matriz[0])):
            elem = ' '+str(matriz[i][j])
            fila += elem
        print(fila)

mi_matriz = [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]]
imprimir_matriz(mi_matriz)


# ##########################################
# FORMAS DE PASAR PARÁMETROS A UNA FUNCIÓN
# ##########################################

def ecuacion_1(a=1,b=5,c=1):
    sol = ((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    return (sol)

# print(ecuacion_1(1,3,2))
# print(ecuacion_1())
# print(ecuacion_1(1,3))
# print(ecuacion_1(a=5))


def parametros(nombre='Ana', apellido='Jurado'):
    print(apellido + ', ' + nombre)

# parametros()
# parametros('Sofía')
# parametros('Pepe', 'García')
# parametros(nombre='Susana')
# parametros(apellido='Noblejas')
# parametros(nombre='Susana', apellido='Griso')
#
# parametros('Pepe', 'García', 'Jhonson')
#     # TypeError: parametros() takes from 0 to 2 positional arguments but 3 were given


def parametros_2(nombre, apellido):
    print(apellido + ', ' + nombre)

# parametros_2()
#     # TypeError: parametros_2() missing 2 required positional arguments: 'nombre' and 'apellido'
# parametros_2('Sofía')
#     # TypeError: parametros_2() missing 1 required positional argument: 'apellido'
# parametros_2('Pepe','García')
#     # OUTPUT: García, Pepe
# parametros_2(apellido='Noblejas')
#     # TypeError: parametros_2() missing 1 required positional argument: 'nombre'
# parametros_2(nombre='Susana')
#     # TypeError: parametros_2() missing 1 required positional argument: 'apellido'
# parametros(nombre='Susana', apellido='Griso')
#     # OUTPUT: Griso, Susana

