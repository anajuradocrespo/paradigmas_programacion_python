# Numeric Types and Operators #

# To complex
# ---------------------------------------------
import datetime
import re

a = 3
complex_a = complex(a)
print('a: ', complex_a, type(complex_a))
# --> (3+0j) <class 'complex'>

b = 7.5
complex_b = complex(b)
print('b: ', complex_b, type(complex_b))
# --> (7.5+0j) <class 'complex'>

# To_int
# ---------------------------------------------
c = 34.54
int_c = int(c)
print('c: ', int_c, type(int_c))
# --> c:  34 <class 'int'>

# d = (3+7j)
# int_d = int(d)
# print('d: ', int_d, type(int_d))
# --> TypeError: can't convert complex to int

# To_float
# ---------------------------------------------
e = 7
float_e = float(e)
print('e: ', float_e, type(float_e))
# --> e:  7.0 <class 'float'>

# f = (7+3j)
# float_f = float(f)
# print('f: ', float_f, type(float_f))
# --> TypeError: can't convert complex to float


# Other operators #
g = abs(-3.5)
h = abs(-456)
i = abs(-3-5j)

j = divmod(34, 7)

k = pow(2, 5)

conjugate = (-3-7j).conjugate()

# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #

hechizo = "Alojomora"
magia = 20

if hechizo == "Expeliarmus":
    magia -= 5
    print('Expeliarmus - Magia: ', magia)

elif hechizo == "Alojomora":
    magia += 5
    print('Alojomora - Magia: ', magia)

else:
    print('Hechizo desconocido')

# --> Alojomora - Magia:  25

# ------------------------------------------------------------------------------------------------------------------- #
altura = 3
for i in range(altura):
    pass

print('\n')

# STRING FORMATTING #

num = 123.45678

print('THE OLD WAY \n')
# Formatting the old way
print('Hello, this number %s is my magical number' %num)        # Whatever go to string
print('Hello, this number %d is my magical number' %num)        # Number to INT
print('Hello, this number %f is my magical number' %num)        # Number to FLOAT with 6 decimals default
print('Hello, this number %.3f is my magical number' %num)      # Specify the number of decimals (3)
print('Hello, this number %10.3f is my magical number' %num)    # Specify the minimun width (10)
print('\n')

print('THE NEW WAY \n')
# Formatting the new way
print(f'Hello, this number {num} is my magical number')
# print(f'Hello, this number {num:d} is my magical number')     # Error
print(f'Hello, this number {num:f} is my magical number')
print(f'Hello, this number {num:.3f} is my magical number')
print(f'Hello, this number {num:10.3f} is my magical number')
print('\n')

print('Other Examples \n')
n = 123456789
print(f'{n:,}')
d = datetime.datetime(1989, 3, 31, 11, 10, 30)
print(f'Mi fecha de nacimiento es {d:%Y-%m-%d %H:%M:%S}')
a = 'Hola holita vecinitos'                                 # len 21
print(f'{a:50} es la famosa frase de Ned Flanders')
print(f'{a:30} es la famosa frase de Ned Flanders')
x = 44
print(f"El numero {x} --> int: {x:d};  hex: {x:x};  oct: {x:o};  bin: {x:b}")


# def caracteres(cadena):
#     d={}
#     for c in cadena:
#         d[c] += d.get(c, 1)
#     return d
#
#
# car = caracteres('Hola que tal!')
# print(car)
#
# # EXPRESIONES REGULARES CLASE
#
# VALIDAR POSICIONES DE AJEDREZ:      ([A-H][1-8])*$
# VALIDAR UN NÚMERO EN HEXADECIMAL:   ([0-9a-fA-F])+$
# Nombre de variable válida:          [-]*[a-z]+[0-0a-zA-Z_]*$
# Contraseña de 8 o más números y letras:                    [0-9a-zA-Z]{8}[0-9a-zA-Z]*$
#
# len(re.findAll(r'\besta\b', cadena))  #Esta estantería está atestada


lista = [1,34,654,7,23,5678]

def format_numbers(lista):
    n = len(max(lista))
    r = []
    for l in lista:
        # added_ceros = pos - len(str(l))
        # num = '0'*added_ceros+str(l)
        r.append(str(e).zfill(n+1))
        return r

frase = 'Hola capitán, mi capitán, "al abordaje" , nwerwer wer "fgfgfg" sfsrf'

# print(re.match(r'".*$"', frase))
#         re.findall(r'".*$"', frase)
#         re.sub
#
# python ejercicio pilas y colas y ver con que estructura
#  crear listas, tuplas, dic vacias. conjunto vacío-> set
# Para inicializar variables mejor con las funciones
#









