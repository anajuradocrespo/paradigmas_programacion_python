# ___________________________________________________________________________________________________________________
# Crear una función que gestione una agenda, permitirá agregar números de teléfono a personas.
# ___________________________________________________________________________________________________________________


class Agenda:

    def __init__(self):
        self.agenda = dict()

    def añadir(self, nombre, telefono):
        self.agenda[nombre] = self.agenda.get(nombre, set()) | {telefono}
                                        # get(key,default) default: value to be returned in case key does not exist
        # con el get, obtenemos un set que representa a los teléfonos
        # con el operador | (union), lo que hacemos es unir los dos conjuntos

    def eliminar(self, nombre, telefono):
        self.agenda[nombre] = self.agenda.get(nombre, set()) - {telefono}


    def esta(self, nombre, telefono):
        return nombre in self.agenda.keys() and telefono in self.agenda[nombre]

    def imprimir_agenda(self):
        for i in self.agenda.items():
            print(i)


# mi_agenda = Agenda()
# print('________________________________')
# mi_agenda.imprimir_agenda()
# print('________________________________')
# mi_agenda.añadir('Pepe', 123456789)
# mi_agenda.añadir('Pepe', 987654321)
# mi_agenda.añadir('Antonia', 123123123)
# mi_agenda.añadir('Benito', 900123123)
# mi_agenda.añadir('Benito', 123321000)
# mi_agenda.añadir('Benito', 900555000)
# print('________________________________')
# mi_agenda.imprimir_agenda()
# print('________________________________')
#
# print(mi_agenda.esta('Benito', 900555000))
# print(mi_agenda.esta('Antonia', 123123123))
#
# mi_agenda.eliminar('Pepe', 987654321)
# mi_agenda.eliminar('Pepe', 987654320)
#
# print(mi_agenda.esta('Pepe', 987654321))
#
# print('________________________________')
# mi_agenda.imprimir_agenda()
# print('________________________________')
