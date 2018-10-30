# -*- coding: utf-8 -*-
#Autor: Héctor Rodolfo Álvarez Dávalos A01636166

import random
from time import sleep 
lista_palabras = 'sopa fruta roca pollo sandia python pulpo fuerza estrella limon cereza toro pizza juego ahorcado luna jabon morza cocodrilo'.split()
ascii_ahorcado =['''
00000000000000000
    0           0
    0           
    0           
    0           
    0          
    0         
    0        
    0          
    0            
    0             
    0       
''',
'''
00000000000000000
    0           0
    0           1
    0          1 1
    0           1
    0          
    0           
    0          
    0          
    0            
    0             
    0       
    0
    0
''',
'''
00000000000000000
    0           0
    0           1
    0          1 1
    0           1
    0           2
    0           2 
    0           2  
    0             
    0              
    0               
    0                
''',
'''
00000000000000000
    0           0
    0           1
    0          1 1
    0           1
    0          32
    0         3 2 
    0        3  2  
    0          
    0            
    0             
    0              
''',
'''
00000000000000000
    0           0
    0           1
    0          1 1
    0           1
    0          324
    0         3 2 4
    0        3  2  4
    0          
    0            
    0             
    0       
    0
''',
'''
00000000000000000
    0           0
    0           1
    0          1 1
    0           1
    0          324
    0         3 2 4
    0        3  2  4
    0          5 
    0         5   
    0        5     
    0       5       
    0
''',
'''
00000000000000000
    0           0
    0           1
    0          1 1
    0           1
    0          324
    0         3 2 4
    0        3  2  4
    0          5 6
    0         5   6
    0        5     6
    0       5       6
    0
''']

def palabra_a_adivinar():
    '''Funcion para obtener una palabra, al azar, de la lista de palabras.'''
    palabra = []
    palabra = lista_palabras[random.randrange(len(lista_palabras)-1)]  
    return palabra

def palabra_display():
    '''Esta funcion genera el display de la palabra, ocultando las letras al usuario.'''
    display = ''
    for i in range(len(palabra_incognita)):
        display += '_'
    return display

palabra_incognita = palabra_a_adivinar()
palabra_guiones = palabra_display()

def otra_partida():
    '''Esta funcion da la opcion de jugar de nuevo, reiniciando el ciclo, o finalizar el programa, dando fin al ciclo del juego'''
    decision = input('Gracias por jugar. Desea comenzar otra partida? a) Si b)No.\nEscriba la letra correspondente a la accion deseada: ').lower()
    decisiones = 'ab'
    while decision not in decisiones:
        decision = input('Entrada no aceptada. Por favor, escriba "a" o "b" para elegir una opcion: ')
        #Esto evita entradas no esperadas por parte del usuario
        
    if decision == 'a':
        return True
    if decision == 'b':
        return False
    #Estos returns son usados para romper o continual con el ciclo, en la seccion del juego.
    
def display_juego(ascii_ahorcado, errores, aciertos, palabra_incognita, palabra_guiones):
    '''Esta funcion muestra el estado actual del juego al usuario, con el dibujo del ahorcado, las letras acertadas y los errores.'''
    
    print(ascii_ahorcado[len(errores)])
    print('Errores: ', end=' ')
    
    for i in errores:
        print(i, end=' ') #Esto muestra los errores al usuario

    print('\nAciertos: ', end=' ')
    for i in aciertos:
       print(i, end=' ') #Esto muestra los aciertos al usuario

    for i in range(len(palabra_incognita)): # sustituye los espacios vacíos con las letras adivinadas
        if palabra_incognita[i] in aciertos:
            palabra_guiones = palabra_guiones[:i] + palabra_incognita[i] + palabra_guiones[i+1:]
            #palabra_guiones[i] = palabra_incognita[i]
            
    for i in palabra_guiones: # muestra la palabra en forma de guiones y actualiza en base a los aciertos
        print('\n',i,end=' ')
       

                    
def intento(entradas_usuario):
    '''Esta funcion se encarga de recibir y validar la entrada del usuario'''    
    while True:
        entrada = input('\nPor favor, introduce una letra: ').lower() 
        if entrada in entradas_usuario:
            print('Letra ya ingresada, por favor ingrese otra.')
        elif entrada not in list('abcdefghijklmnopqrstuvwxyz'):
            print('Entrada no aceptada, por favor introduce una letra.')
        elif len(entrada) >= 2 or len(entrada) <=0:
            print('Entrada no aceptada, por favor introduce una letra.')
        else:
            return entrada
                                                            
errores = ''
aciertos = ''
juego_en_curso = True

print('''Bienvenido a: \n
 █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗ 
██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║
██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║
██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝

El clasico juego de adivinanzas.
A continuacion aparecera una serie de guiones y usted debera adividar la palabra con el numero de letras correspondiente.

Si logra adivinar la palabra antes de que se complete la figura del ahorcado, ganara; sino perdera.

Suerte!''')

sleep(8)
#Esto da tiempo al usuario de leer las instrucciones.

while True:
    display_juego(ascii_ahorcado, errores, aciertos, palabra_incognita, palabra_guiones)
    guess = intento(errores + aciertos)
    
    if guess in palabra_incognita:
        aciertos += guess
        palabra_adivinada = True
        for i in range(len(palabra_incognita)):
            if palabra_incognita[i] not in aciertos:
                palabra_adivinada = False
                break
        if palabra_adivinada == True:
            print(f'\nHas ganado. La palabra era "{palabra_incognita}". Vuelve pronto.')
            juego_en_curso = False
    else:
        errores += guess
        if len(errores) == len(ascii_ahorcado)-1:
            display_juego(ascii_ahorcado, errores, aciertos, palabra_incognita, palabra_guiones)
            print(f'\nHas perdido. La palabra era {palabra_incognita}. Suerte para la proxima.')
            juego_en_curso = False

    if juego_en_curso == False:
        if otra_partida() == True:
            juego_en_curso = True
            errores = ''
            aciertos = ''
            entradas_usuario = ''
            palabra_incognita = palabra_a_adivinar()
        else:
            break

print('\nGracias por usar el programa, vuelve pronto.')

#En esta actividad, practique el uso de la combinacion de funciones, el uso de strings, los ciclos for y las listas.
