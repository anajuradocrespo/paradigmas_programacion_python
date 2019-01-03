# ___________________________________________________________________________________________________________________
# Reimplementar la función del calculo de los 100 primeros primos haciendo uso de conjuntos.
# ___________________________________________________________________________________________________________________
import random
from copy import copy
from math import floor, sqrt

def generar_primos_pro(limite):
    # lst = [x for x in range(1, limite+1) if es_primo_pro(x)]
    set_primos = set()
    for i in range(1, limite + 1):
        if es_primo_pro(i):
            set_primos.add(i)
    return set_primos

def es_primo_pro(num):
    for j in range(2, floor(sqrt(num))+1):
        # Con esto genero los divisores que han de ir de 2 a (raíz del número)+1 (para que lo coja el rango)
        if num % j == 0:
            return False
    return True

# print(generar_primos_pro(101))


# ___________________________________________________________________________________________________________________
# Crear una función que recibe un número y devuelve una lista con sus dígitos.
# ___________________________________________________________________________________________________________________
def lista_digitos(num):
    lst = [int(x) for x in str(num)]
    return lst

# print(lista_digitos(1243))


# ___________________________________________________________________________________________________________________
# Un número es cubifinito si al elevar al cubo sus dígitos y sumarlos da como resultado 1 u otro número cubifinito.
# Crear una función que reciba un número y devuelva si es cubifinito.
# ___________________________________________________________________________________________________________________
def cubifinito(num):
    resultado = sum([int(x)**3 for x in str(num)])
    # if resultado == 1:
    #     return True
    # elif sum([int(x)**3 for x in str(resultado)]) == 1:
    #     return True
    # else:
    #     return False
    return resultado == 1 or cubifinito(resultado) == 1

# print(cubifinito(8741))   # TRUE 1243, 10, 87418


# ___________________________________________________________________________________________________________________
# Implementar las funciones sobre conjunto, unión, intersección, diferencia y copia.
# ___________________________________________________________________________________________________________________
def union(conj1, conj2):
    union = set()
    for i in conj1:
        union.add(i)
    for j in conj2:
        union.add(j)
    return union

def union_pro(A, B):
    # return A.union(B)
    return A | B


# print(union(conj1={1, 2, 3, 4, 5}, conj2={4, 5, 6, 7, 8}))
# print(union_pro(A={1, 2, 3, 4, 5}, B={4, 5, 6, 7, 8}))

def interseccion(conj1, conj2):
    interseccion = set()
    for i in conj1:
        if i in conj2:
            interseccion.add(i)
    return interseccion

def interseccion_pro(A, B):
    #return A.intersection(B)
    return A & B

# print(interseccion(conj1={1, 2, 3, 4, 5}, conj2={4, 5, 6, 7, 8}))
# print(interseccion_pro(A={1, 2, 3, 4, 5}, B={4, 5, 6, 7, 8}))


def diferencia(conj1, conj2):
    diferencia = set()
    for i in conj1:
        if i not in conj2:
            diferencia.add(i)
    return diferencia

def diferencia_pro(A, B):
    #return A.difference(B)
    return A - B

# print(diferencia(conj1={1, 2, 3, 4, 5}, conj2={4, 5, 6, 7, 8}))
# print(diferencia_pro(A={1, 2, 3, 4, 5}, B={4, 5, 6, 7, 8}))


def copia(conj):
    copia = set()
    for i in conj:
        copia.add(i)
    return copia

def copia_pro(A):
    return A.copy()

# print(copia(conj={1, 2, 3, 4, 5}))
# print(copia_pro(A={1, 2, 3, 4, 5}))



# ___________________________________________________________________________________________________________________
# En una lista hay números en parejas, positivos y negativos (si está el 3, está el -3) pero en posiciones desconocidas.
# Todos los números tienen su pareja de signo opuesto excepto uno.
# Crea una función que dada una lista de este tipo, devuelva el elemento desparejado.
# ___________________________________________________________________________________________________________________

def cada_oveja_con_su_paraje(lista):

    lista_aux = list()

    for j in lista:
        if j not in lista_aux:
            if (-1*j) not in lista_aux:
                lista_aux.append(j)
            else:
                lista_aux.remove((-1*j))
        else:
            lista_aux.append(j)

    return lista_aux

# print(cada_oveja_con_su_paraje([-1,4,-2,1,7,-4,2,2]))


# ___________________________________________________________________________________________________________________
# En una lista de números, todos están repetidos excepto uno.
# Crea una función que devuelva el número no repetido.
# ___________________________________________________________________________________________________________________
def devolver_repetidos(lista):

    # Encontrar el elemento que se repite
    repetido = set()
    if lista[0] == lista[1]:
        repetido.add(lista[0])
    elif lista[0] != lista[1] and lista[0] == lista[2]:
        repetido.add(lista[0])
    else:
        repetido.add(lista[1])

    # Usamos la diferencia de conjuntos
    no_repetido = set(lista) - repetido

    return no_repetido.pop() # pop para que nos devuelva el elemento, no un conjunto con el elemento dentro

#print(devolver_repetidos([7,2,7,7,7,7,7,7]))

# VERSIÓN CLASE
def single(l):
  c=set()
  for e in l:
    if e not in c:
      c.add(e)
    else:
      c.remove(e)
  return c.pop()


# VERSIÓN DE CLASE. NO FUNCIONA
def single_mal(lista):
    s = 0
    for e in lista:
        #XOR de binarios y anula los que son iguales
        s ^= e
    return s

#print(single([7,2,7,7,7,7,7,7]))  # output = 5


# ___________________________________________________________________________________________________________________
# Dado un conjunto de números, devolver una tupla con 2 conjuntos,
# el primero contendrá los pares y el segundo los impares.
# ___________________________________________________________________________________________________________________
def par_impar_tupla(conjunto):

    impares = set()
    pares = set()

    for i in conjunto:
        if i % 2 != 0:
            impares.add(i)
        else:
            pares.add(i)

    return pares, impares

# print(par_impar_tupla(conjunto={1,3,5,6,4,8,6,4,25,5,3,2,6,7,99,20,-35}))


# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el conjunto potencia.
# ___________________________________________________________________________________________________________________
def powerset(lista):

    # Caso base
    if not lista:
        return [[]]

    # Separamos un elemento del resto de la lista
    elemento = lista[0]

    # Hacemos llamada recursiva con el resto de la lista
    # incomplete_pset tiene todos los subconjuntos del resto de la lista
    incomplete_pset = powerset(lista[1:])

    # Ahora tenemos que "generar" los subconjuntos que incluyan al elemento que separamos antes.
    # Estos nuevos subconjuntos los vamos a guardar en subc_ele
    subc_ele = []

    # A cada subconjunto le añadimos el elemento
    for subconjunto in incomplete_pset:
        subc_ele.append([elemento] + subconjunto)

    # Finalmente devolvovemos el nuevo subconjunto (subc_ele) junto con el anterior (incomplete_pset)
    return subc_ele + incomplete_pset

# print(powerset(lista=[1,2,3]))


def powerset_pro(lista):

    # Caso base
    if not lista:
        return [[]]

    # Separamos un elemento del resto de la lista
    elemento = lista[0]

    # Hacemos llamada recursiva con el resto de la lista
    # incomplete_pset tiene todos los subconjuntos del resto de la lista
    incomplete_pset = powerset(lista[1:])

    # Ahora tenemos que "generar" los subconjuntos que incluyan al elemento que separamos antes.
    # Estos nuevos subconjuntos los vamos a guardar en subc_ele
    # A cada subconjunto de incomplete_pset le añadimos el elemento
    subc_ele = [[elemento] + subconjunto for subconjunto in incomplete_pset]

    # Finalmente devolvovemos el nuevo subconjunto (subc_ele) junto con el anterior (incomplete_pset)
    return subc_ele + incomplete_pset

# print(powerset_pro(lista=[1,2,3]))


# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el conjunto cartesiano de dos conjuntos
# (conjunto con todos los pares del primero con el segundo).
# ___________________________________________________________________________________________________________________
def producto_cartesiano(c1, c2):
    p_cart = list()
    for i in c1:
        for j in c2:
            sub_p = set()
            sub_p.update([i, j])
            p_cart.append(sub_p)
    return p_cart


# print(producto_cartesiano(c1={1, 2, 3}, c2={100, 200, 300}))

# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el número de apariciones de cada carácter en una cadena.
# ___________________________________________________________________________________________________________________
def numero_apariciones_caracter(cadena):

    apariciones = dict()
    for c in cadena:
        if c not in apariciones.keys():
            apariciones[c] = 1
        else:
            apariciones[c] += 1
    return apariciones


# print(numero_apariciones_caracter('HOLA CARACOLA'))


# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el número de apariciones de  cada palabra en una frase.
# ___________________________________________________________________________________________________________________
def numero_apariciones_palabra(cadena):

    # Limpiamos la cadena de caracteres que no nos interesan
    prescindible_char = [',', '.', '!', '¡', '?', '¿', 'º', '"']
    clean_cadena = str()
    for c in cadena:
        if c not in prescindible_char:
            clean_cadena += c

    # Saco una lista de las palabras
    palabras = clean_cadena.split(' ')

    # Guardamos el numero de veces que aparecen en un diccionario
    apariciones = dict()
    for p in palabras:
        if p not in apariciones.keys():
            apariciones[p] = 1
        else:
            apariciones[p] += 1
    return apariciones


# print(numero_apariciones_palabra('Esto es una frase para contar!!! el numero? si si numero 989 de apariciones de las palabras. palabras, de palabras'))

# ___________________________________________________________________________________________________________________
# Utilizando el modulo random, crear una función que simule N tiradas de 2 dados
# y cuente las veces que aparece un resultado.
# ___________________________________________________________________________________________________________________
def simular_dados(dados, tiradas):
    """
    Simula tiradas de dados

    :param int dados: número de dados
    :param int tiradas: número de tiradas a simular
    :return dict resultados:  resultados y las veces que ha salido
    """
    rango = dados*6

    resultados = dict()

    for i in range(tiradas):
        # Realizamos la "tirada"
        res = random.randrange(1, rango, 1)  # random.randrange(start, stop[, step])

        # Actualizamos la información en el diccionario de resultados
        if res in resultados.keys():
            resultados[res] += 1
        else:
            resultados[res] = 1

    return resultados


# print(simular_dados(3, 10))


# ___________________________________________________________________________________________________________________
# Crear una función que devuelva el diccionario inverso.
# ___________________________________________________________________________________________________________________
def diccionario_inverso(diccionario):

    dic_keys = list()
    dic_values = list()
    for i in diccionario.keys():
        dic_keys.append(i)
    for j in diccionario.values():
        dic_values.append(j)

    reversed_dic = dict(zip(dic_values, dic_keys))

    return reversed_dic


def diccionario_inverso_2(diccionario):

    list_key_values = list(diccionario.items())
    list_key_values_unzip = list(zip(*list_key_values))
    reversed_dic = dict(zip(list_key_values_unzip[1], list_key_values_unzip[0]))

    return reversed_dic

# mi_diccionario = {'clave_1':'a', 'clave_2':'b', 'clave_3':'c', 'clave_4':'d'}
# print(diccionario_inverso(mi_diccionario))
# print(diccionario_inverso_2(mi_diccionario))




