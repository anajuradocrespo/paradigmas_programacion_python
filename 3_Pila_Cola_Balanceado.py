"""
Ejercicios:
– Implementar las funciones:
    apilar(pila, elemento)
    desapilar(pila)
    cima(pila)
Que simulan una pila usando una lista.

– Implementar las funciones:
    encolar(cola, elemento)
    desencolar(cola)
    primero(cola)
Que simulan una cola usando una lista.

"""
from collections import deque


class Pila:
    """
    Clase Pila. Se introduce y se saca por el mismo sitio. La forma fácil con una lista es hacerlo por el final.
    """

    def __init__(self):
        self.pila = list()


    def apilar(self, elemento):
        """
        Introduce un nuevo elemento en la pila. Inserta el elemento por el final de la lista.
        :param elemento: elemento que va a ser insertado
        """
        self.pila.append(elemento)

    def desapilar(self):
        """
        Quita el último elemento insertado de la pila. Borra el último elemento de la lista.
        """
        self.pila.pop()

    def cima(self):
        """
        Devuelve el elemento de la cima. El último elemento de la lista.
        :return: elemento
        """
        return self.pila[-1]

    def print_pila(self):

        print(self.pila)

    def size_pila(self):
         return len(self.pila)


class Cola:
    """
    Clase Cola. Se introduce por cabecera y se extrae por el final. Implementada con listas.
    """

    def __init__(self):
        self.cola = list()

    def encolar(self, elemento):
        """
        Introducimos elemento por cabecera. Se introduce al principio de la lista. INEFICIENTE.
        :param elemento: elemento
        """
        self.cola.insert(0, elemento)

    def desencolar(self):
        """
        Extraer elemento por el final. Se extrae por el final de la lista.
        El final de la lista es el principio de la cola.
        """
        self.cola.pop()

    def primero(self):
        """
        Devuelve el primer elemento de la lista.
        :return: elemento
        """
        return self.cola[-1]

    def print_cola(self):
        print(self.cola)


# # PARA PROBAR LOS MÉTODOS DE LA CLASE
# print('PILA')
# mi_pila = Pila()
# mi_pila.apilar('a')
# mi_pila.apilar('b')
# mi_pila.apilar('c')
# mi_pila.apilar('d')
# mi_pila.print_pila()
# print(mi_pila.cima())
# mi_pila.desapilar()
# print(mi_pila.cima())
# mi_pila.print_pila()
#
# print('________________________')

# # PARA PROBAR LOS MÉTODOS DE LA CLASE
# print('COLA')
# mi_cola = Cola()
# mi_cola.encolar('f')
# mi_cola.encolar('g')
# mi_cola.encolar('h')
# mi_cola.print_cola()
# print(mi_cola.primero())
# mi_cola.desencolar()
# mi_cola.print_cola()
# print(mi_cola.primero())
#
# print('________________________')




class ColaDeque:

    def __init__(self):
        self.colad = deque()

    def encolar(self, elemento):
        """
        Introducimos elemento por cabecera. Se introduce al principio de la lista.
        :param elemento: elemento
        """
        self.colad.appendleft(elemento)

    def desencolar(self):
        """
        Extraer elemento por el final. Se extrae por el final de la lista.
        El final de la lista es el principio de la cola.
        """
        self.colad.pop()

    def primero(self):
        """
        Devuelve el primer elemento de la lista.
        :return: elemento
        """
        return self.colad[-1]

    def print_cola(self):
        print(self.colad)


# # PARA PROBAR LOS MÉTODOS DE LA CLASE
# print('COLADEQUE')
# mi_cola = ColaDeque()
# mi_cola.encolar('f')
# mi_cola.encolar('g')
# mi_cola.encolar('h')
# mi_cola.print_cola()
# print(mi_cola.primero())
# mi_cola.desencolar()
# mi_cola.print_cola()
# print(mi_cola.primero())
#
# print('________________________')


"""
Implementa un programa que devuelva si en una cadena que
recibe de entrada, los paréntesis que en ella aparecen están
balanceados.
"""


def balanceado(cadena):
    parentesis = Pila()
    for elemento in cadena:
        if elemento == "(":
            Pila.apilar(parentesis, elemento)
        elif elemento == ")":
            if parentesis.size_pila() != 0:
                Pila.desapilar(parentesis)

    return parentesis.size_pila() == 0


print(balanceado(" esto es ( una cadena) de () prueba (( dpdc ) cfsjfsf )  "))
