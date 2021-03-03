from Tarea1 import check_char
from Tarea1 import caps_switch
import pytest

'''Se parametrizan los caracteres de A-Z y a-z para poder correr
las pruebas con muchos valores de entrada'''


@pytest.mark.parametrize("par, out", [('A', 0), ('B', 0), ('C', 0), ('D', 0),
                                      ('E', 0), ('F', 0), ('G', 0), ('H', 0),
                                      ('I', 0), ('J', 0), ('K', 0), ('L', 0),
                                      ('M', 0), ('N', 0), ('O', 0), ('P', 0),
                                      ('Q', 0), ('R', 0), ('S', 0), ('T', 0),
                                      ('U', 0), ('V', 0), ('W', 0), ('X', 0),
                                      ('Y', 0), ('Z', 0), ('a', 0), ('b', 0),
                                      ('c', 0), ('d', 0), ('e', 0), ('f', 0),
                                      ('g', 0), ('h', 0), ('i', 0), ('j', 0),
                                      ('k', 0), ('l', 0), ('m', 0), ('n', 0),
                                      ('o', 0), ('p', 0), ('q', 0), ('r', 0),
                                      ('s', 0), ('t', 0), ('u', 0), ('v', 0),
                                      ('w', 0), ('x', 0), ('y', 0), ('z', 0)])
def test_answer1(par, out):

    '''Se verifica que la funcion check_char retorne 0 para todos los
    caracteres dentro del rango A-Z y a-z'''

    assert check_char(par) == out


'''Se parametrizan los caracteres de A-Z y a-z para poder correr
las pruebas con los valores de entrada esperados a dar
un caso de éxito'''


@pytest.mark.parametrize("MAY, minu", [('A', 'a'), ('B', 'b'), ('C', 'c'),
                                       ('D', 'd'), ('E', 'e'), ('F', 'f'),
                                       ('G', 'g'), ('H', 'h'), ('I', 'i'),
                                       ('J', 'j'), ('K', 'k'), ('L', 'l'),
                                       ('M', 'm'), ('N', 'n'), ('O', 'o'),
                                       ('P', 'p'), ('Q', 'q'), ('R', 'r'),
                                       ('S', 's'), ('T', 't'), ('U', 'u'),
                                       ('V', 'v'), ('W', 'w'), ('X', 'x'),
                                       ('Y', 'y'), ('Z', 'z'), ('a', 'A'),
                                       ('b', 'B'), ('c', 'C'), ('d', 'D'),
                                       ('e', 'E'), ('f', 'F'), ('g', 'G'),
                                       ('h', 'H'), ('i', 'I'), ('j', 'J'),
                                       ('k', 'K'), ('l', 'L'), ('m', 'M'),
                                       ('n', 'N'), ('o', 'O'), ('p', 'P'),
                                       ('q', 'Q'), ('r', 'R'), ('s', 'S'),
                                       ('t', 'T'), ('u', 'U'), ('v', 'V'),
                                       ('w', 'W'), ('x', 'X'), ('y', 'Y'),
                                       ('z', 'Z')])
def test_answer2(MAY, minu):

    '''Se verifica que la funcion caps_switch retorne la letra
    invertida (pasar de mayúscula a minúscula y viceversa)
    para todos los caracteres dentro del rango A-Z y a-z'''

    assert caps_switch(MAY) == minu


def test_answer3():

    '''Se verifica que se obtenga el error 3 al ingresarle a la funcion
    check_char un string con más de 1 caracter'''

    assert check_char('abc') == 'Error 3'


def test_answer4():

    '''Se verifica que se obtenga el error 2 al ingresarle a la funcion
    check_char un string con caracteres fuera de A-Z y a-z'''

    assert check_char('3') == 'Error 2'


def test_answer5():

    '''Se verifica que se obtenga el error 1 al ingresarle a la funcion
    check_char un parámetro que no es un string'''

    assert check_char(1.5) == 'Error 1'
