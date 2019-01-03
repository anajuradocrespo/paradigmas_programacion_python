# ___________________________________________________________________________________________________________________
# Crear una función que escribe una cadena en Morse.
# ___________________________________________________________________________________________________________________


# ___________________________________________________________________________________________________________________
# Crear la función inversa, de una cadena en Morse devuelve la traducción.
# ___________________________________________________________________________________________________________________

class Morse:

    string_morse_dic = {'A': '.-',
                        'B': '-...',
                        'C': '-.-.',
                        'D': '-..',
                        'E': '.',
                        'F': '..-.',
                        'G': '--.',
                        'H': '....',
                        'I': '..',
                        'J': '.---',
                        'K': '-.-',
                        'L': '.-..',
                        'M': '--',
                        'N': '-.',
                        'O': '---',
                        'P': '.--.',
                        'Q': '--.-',
                        'R': '.-.',
                        'S': '...',
                        'T': '-',
                        'U': '..-',
                        'V': '...-',
                        'W': '.--',
                        'X': '-..-',
                        'Y': '-.--',
                        'Z': '--..',
                        '0': '-----',
                        '1': '.----',
                        '2': '..---',
                        '3': '...--',
                        '4': '....-',
                        '5': '.....',
                        '6': '-....',
                        '7': '--...',
                        '8': '---..',
                        '9': '----.',
                        }

    def string_to_morse(self, cadena):

        cadena_en_morse = str()
        for c in cadena:
            if c in self.string_morse_dic.keys():
                cadena_en_morse += self.string_morse_dic[c]+'/'
            else:
                cadena_en_morse += c

        return cadena_en_morse

    def morse_to_string(self, cad_mor):
        # Lo normal sería crear el diccionario inverso sólo una ves y tenerlo como una varaible (como está el otro)
        # De esta forma estamos creando un diccionario inverso cada vez que llamamos a esta función

        morse_string_dic = self.diccionario_inverso_2(self.string_morse_dic)

        cadena_en_str = str()

        # Quitemos los espacios y separamos las letras morse por el caracter /
        letras_morse = cad_mor.replace(' ', '')
        letras_morse = letras_morse.split('/')

        for m in letras_morse:
            if m in morse_string_dic.keys():
                cadena_en_str += morse_string_dic[m]
            else:
                cadena_en_str += m

        return cadena_en_str

    def diccionario_inverso_2(self, diccionario):
        list_key_values = list(diccionario.items())
        list_key_values_unzip = list(zip(*list_key_values))
        reversed_dic = dict(zip(list_key_values_unzip[1], list_key_values_unzip[0]))

        return reversed_dic


# traduccion = Morse()
# mi_cadena = 'HOLA ANA'
# mi_cadena_morse = '..../---/.-../.-/ .-/-./.-/'
# print(traduccion.string_to_morse(mi_cadena))
# print(traduccion.morse_to_string(mi_cadena_morse))
#
# mi_diccionario_inverso = traduccion.diccionario_inverso_2(traduccion.string_morse_dic)
# print(mi_diccionario_inverso)
