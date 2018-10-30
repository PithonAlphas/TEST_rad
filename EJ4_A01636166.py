#Autor: Héctor Rodolfo Álvarez Dávalos A01636166

print('¡Bienvenido a la calcuradora de interés simple!')
year = int(input('Por favor, ingrese el número de años del interés: '))
cantidad = float(input('A continuación, ingrese la cantidad a pagar: '))
interes = float(input('Finalmente, ila tasa de interés: '))

interes_simple = (year*cantidad*interes)/100
print("El interés simple es {0:7.2f}$".format(interes_simple))

#La fórmula de interés simple fue obtenida en la instrucción del ejercicio 4, de la presentación 4 del curso.
#Para usar el formato tipo 'printf' use la guia de este sitio: https://www.python-course.eu/python3_formatted_output.php
#En esta practica aprendí sobre el uso de outputs con formato en python y los distintos tipos de formato que se pueden usar con esta función
