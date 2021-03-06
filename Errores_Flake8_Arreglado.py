'''Código realizado por Milton Esteban Cárdenas Fley
y Sebastián Picado González Estudiantes de Ingeniería
en Mecatrónica en el Instituto Tecnológico de Costa Rica.
Con el propósito de crear muchos errores detectables en flake8.
Unos caracteres más que hicieron falta'''

import time  # Se importa el módulo time

time.sleep(2)  # Pausa de 2 segundos
b = "Profesor, en este código hay varios "  # Se guarda el mensaje
c = "errores detectables por flake8"  # Se guarda el mensaje
print(b+c)  # Se imprime b concatenado a c
time.sleep(1)  # Pausa de 1 segundo
print("Lo que lo convierte en un código peligroso")  # Se imprime el mensaje
time.sleep(2)  # Pausa de 2 segundos
print("...")  # Se imprime el mensaje
time.sleep(2)  # Pausa de 2 segundos
print("Si desea continuar es bajo su propio riesgo")  # Se imprime el mensaje
time.sleep(3)  # Pausa de 3 segundos
print("Presione 1 para continuar sino presione 0")  # Se imprime el mensaje
a = input("")  # Se recibe en la variable "a" lo ingresado por el usuario

'''Se analiza si el usuario ingresó los valores esperados'''

if a == str(1) or a == str(0):
    time.sleep(1.5)  # Pausa de 1,5 segundos
    print("Final Bueno")  # Se imprime el mensaje
    time.sleep(1)  # Pausa de 1 segundo
    d = "Procederé a definir funciones con el "  # Se guarda el mensaje
    e = "único propósito de crear más errores"  # Se guarda el mensaje
    print(d+e)  # Se imprime d concatenado a e

else:
    time.sleep(1.5)  # Pausa de 1,5 segundos
    print("Rumpeltinzky, eso no era parte del trato")  # Se imprime el mensaje
    time.sleep(1.5)  # Pausa de 1,5 segundos
    f = "Debido al exceso de errores "  # Se guarda el mensaje
    g = "el programa va a colapsar"  # Se guarda el mensaje
    print(f+g)  # Se imprime f concatenado a g
    time.sleep(2)  # Pausa de 1,5 segundos
    h = "Se acabó Anakin, "  # Se guarda el mensaje
    i = "llevo la delantera de errores"  # Se guarda el mensaje
    print(h+i)  # Se imprime h concatenado a i


def main():  # Se crea la función main
    j = "La idea de esta función era "  # Se guarda el mensaje
    k = "desbloquear más errores detectables por "  # Se guarda el mensaje
    m = "flake 8"
    print(j+k+m)  # Se imprime j concatenado a k y a l
