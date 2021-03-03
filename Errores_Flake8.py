'''Código realizado por Milton Esteban Cárdenas Fley y Sebastián Picado González
Estudiantes de Ingeniería en Mecatrónica en el Instituto Tecnológico de Costa Rica
Con el propósito de crear muchos errores detectables en flake8. Unos caracteres más que hicieron falta'''
import time #Se importa el módulo time, la que permite usar funciones de tiempo




time.sleep(2) #El programa espera 2 segundos para ejecutar el siguiente comando 
print ("Profesor, en este código hay varios errores detectables por flake8") #Se imprime el mensaje a la pantalla del usuario
time.sleep(1)#El programa espera 1 segundo para ejecutar el siguiente comando 

print ("Lo que lo convierte en un código peligroso")#Se imprime el mensaje a la pantalla del usuario
time.sleep (2)#El programa espera 2 segundos para ejecutar el siguiente comando 
print ("...")#Se imprime el mensaje a la pantalla del usuario



time.sleep (2)#El programa espera 2 segundos para ejecutar el siguiente comando 
print ("Si desea continuar es bajo su propio riesgo") #Se imprime el mensaje a la pantalla del usuario
time.sleep (3)#El programa espera 3 segundos para ejecutar el siguiente comando 



print("Presione 1 para continuar sino presione 0")#Se imprime el mensaje a la pantalla del usuario
a=input("")#Se recibe en la variable a lo ingresado por el usuario


'''Se usa el condicional para analizar si el usuario ingresó los valores esperados de 1 o 0'''

if a==str(1) or a==str(0):
    time.sleep(1.5)#El programa espera 1,5 segundos para ejecutar el siguiente comando 
    print ("Final Bueno") #Se imprime el mensaje a la pantalla del usuario
    time.sleep(1) #El programa espera 1 segundos para ejecutar el siguiente comando
    print("Procederé a definir funciones con el único propósito de crear más errores") #Se imprime el mensaje a la pantalla del usuario
    
else:
    time.sleep(1.5) #El programa espera 1,5 segundos para ejecutar el siguiente comando 
    print ("Rumpeltinzky, eso no era parte del trato") #Se imprime el mensaje a la pantalla del usuario
    time.sleep(1.5) #El programa espera 1,5 segundos para ejecutar el siguiente comando 
    print ("Debido al exceso de errores el programa va a colapsar")#Se imprime el mensaje a la pantalla del usuario
    time.sleep(2)#El programa espera 1,5 segundos para ejecutar el siguiente comando 
    print ("Se acabó Anakin, llevo la delantera de errores") #Se imprime el mensaje a la pantalla del usuario
def main():#Se crea la función main
    print("Realmente la idea de esta función era desbloquear más errores detectables por flake 8")#Se imprime el mensaje a la pantalla del usuario    
