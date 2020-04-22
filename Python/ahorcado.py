# Esto es el juego del ahorcado para practicar el lenguaje de programación Pyhton.

# 1º. Pedimos una palabra que el contrincante debe de adivinar.

palabra = input('Introduzca una palabra: ')

milista = [] # Creo una lista donde metemos la palabra para poder recorrerla despues.
milista.append(palabra) # Introducimos la palabra escrita dentro de la lista.
cont = len(palabra) # Contamos los caracteres de la palabra.

for e in range(cont):
    cambio = palabra.replace(palabra, '_ ')
    print (cambio, end='')


def aciertos():
    vida = 5                                            # marcamos 5 vidas al inicio
    nuevaletra = ''                                     # guardamos una variable vacia donde mas adelante guardaremmos letra a letra introducida.
    while vida > 0:
        fallos = 0                                      # Fallos a 0 para empezar 
        for letra in palabra:                           # buscamos la letra en la palabra
            if letra in nuevaletra:                     # si esta imprimimos la letra
                print (letra, end='')
            else:
                print (cambio, end='')                   # si no esta imprimimos los giones.
                fallos+=1
        if fallos == 0:                                  # si fallos llega a 0 hemos ganados y salimos del juego
            print ('\n\nGanaste')
            break

        letra = input('\n\nIntroduzca una letra: ')
        nuevaletra += letra

        if letra not in palabra:                         # Si la letra no esta en la palabra restamos una vida
            vida-=1
            print ('\nError...')
            print ('\nTe quedad ' + str(vida) + ' vidas.')
        if vida == 0:                                      # si la vida llega a 0 hemos perdido.
            print ('\nPerdiste... :(')
    else:
        print ('\nGracias por jugar')
aciertos()

    




