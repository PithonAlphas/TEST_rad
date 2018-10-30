#Autor: Héctor Rodolfo Álvarez Dávalos A01636166

print('¡Bienvenido a la calculadora de resistencia total!')
res1 = float(input('Por favor, ingrese el valor de su primera resistencia: '))
res2 = float(input('A continuación, ingrese el valor de su segunda resistencia: '))
res3 = float(input('Fimanalmente, ingrese el valor de su tercera resistencia: '))
res_total = 1/((1/res1)+(1/res2)+(1/res3))

print('La resistencia total es ', res_total,' ohms.')

#La fórmula fue obtenida en la instrucción del ejercicio 9, de la presentación 4 del curso.
#En esta práctica, practiqué la jerarquía de operaciones.
