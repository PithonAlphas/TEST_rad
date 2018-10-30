#-*- coding: utf-8 -*-

'''
Hecho por:

Agustín Salvador Quintanar de la Mora        A01636142
Hector Rodolfo Alvarez Dávalos               A01636166


'''
import math

print('''

Bienvenid@ al solucionador de ecuaciones cuadraticas

La forma de la ecuación cuadratica es: Ax^2 + Bx + C = 0
''')

a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))

print('')
print('Ecuación cuadrática:',str(a)+'x^2 +',str(b)+'x +',str(c),'= 0')
if a == 0:
    if b == 0:
        print('No es una ecuación')
    else:
        x == -b/c
    print('X =',x)

else:

    if b**2 - 4*a*c < 0 :

        print('La solución de la ecuación es imaginaria')

        x1 = complex(-b/(2*a),math.sqrt(abs(b**2-4*a*c))/(2*a))
        print('X1 =',x1.real,'+',x1.imag,'i')

        x2 = complex(-b/(2*a),math.sqrt(abs(b**2-4*a*c))/(-2*a))
        print('X2 =',x2.real, x2.imag,'i')


    elif b**2 - 4*a*c > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

        print('X1 =',x1)
        print('X2 =',x2)

    else:
        print('Ambas raices son iguales a:',-b/2*a)

#Practicamos el uso de condicionales, y aprendimos a usar el tipo de datos complejos de Python.