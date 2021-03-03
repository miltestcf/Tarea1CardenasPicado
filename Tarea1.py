def check_char(a):

    ''' Una vez recibido el parámetro "a", se debe verificar
    (mediante estructuras condicionales) que pertenezca a la
    categoría de string, que no posea caracteres fuera del rango
    A-Z o a-z y que solo esté compuesto de un único caracter. En
    caso contrario, se retorna un código de error definido.'''

    if type(a) == str:
        if str.isalpha(a) is False:

            return 'Error 2'

            '''El parámetro recibido posee uno o más caracteres que
            no se encuentran dentro del rango A-Z o a-z'''

        else:

            if len(a) != 1:

                return 'Error 3'  # Parámetro recibido posee más de un caracter

            else:

                return 0  # Se retorna 0 al cumplir todos los requerimientos

    else:

        return 'Error 1'  # El parámetro recibido no es un string


def caps_switch(s):

    ''' Una vez recibido el parámetro "s", se le envía a
    la función  check_char() con el propósito de verificar
    si se recibió un único carácter entre A-Z.'''

    '''En caso de que se cumpla con que se recibió un único
    carácter entre A-Z, se utiliza swapcase() para pasar
    las letra en mayúscula a minúscula y viceversa.'''

    if check_char(s) == 0:

        s = str.swapcase(s)

        return s  # Letra invertida (de mayúscula a minúscula o viceversa)

        '''En caso de que no se cumpla con que se recibió
        un único carácter entre A-Z, se retorna el mismo
        error que retorna la función check_char()'''

    else:

        return check_char(s)  # Retorna error encontrado en check_char()
