# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bucles_for.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/09 20:35:28 by marvin            #+#    #+#              #
#    Updated: 2024/03/09 20:35:28 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# bucles for para practicar
# en los bucles for es comun usar la función range(inicio, parada, paso)

# def numeros_pares():
# 	for x in range(0, 100 + 1, 2):
# 		print(x)
# numeros_pares()

# def fizzbuzz():
# 	for x in range(0, 100 + 1):
# 		if x % 3 == 0 and x % 5 == 0:
# 			print("fizzbuzz")
# 		elif x % 5 == 0:
# 			print("buzz")
# 		elif x % 3 == 0:
# 			print("fizz")
# 		else:
# 			print(str(x))
# 		x += 1
# fizzbuzz()

#en esta funcion crearemos una piramide de numeros como si fuera un domino
# def	piramide_numerica(num):
# 	for izq in range(num):
# 		for der in range(izq, num):
# 			print("[" + str(izq) + "|" + str(der) + "]", end=" ")
# 		print()
# piramide_numerica(10)

#funcion que recibe un numero de equipos y los enfrenta sin repetir(no sortea, lo hace en orden)
# def	sorteo_equipos(num_equipos):
# 	equipos = ["Equipo" + str(x) for x in range(1,num_equipos + 1)]
# 	for equipo_local in equipos:
# 		for equipo_visitante in equipos:
# 			if equipo_local != equipo_visitante:
# 				print(equipo_local + " vs " + equipo_visitante)
# sorteo_equipos(8)

#funcion que imprime una string caracter a caracter en 2 variantes
# def imprimir_caracter(string):
# 	for c in string:
# 		print("el caracter de la string es " + c)
		
# imprimir_caracter("cancamusa")

# def imprimir_caracter2(string):
# 	c = 0
# 	while c < len(string):
# 		print("caracter =" + string[c])
# 		c += 1
# imprimir_caracter("cancamusa")

#funcion que nos devuelve la posicion de los caracteres de una string
# def imprimir_pos(string):
#     for i in range(len(string)+1):
#         print(i)
# imprimir_pos("cancamusa")

#y en esta funcion siguiente haremos las dos cosas a la vez, pos y char 
#usando la funcion enumerate
def imp_char_y_pos(string):
    for i, char in enumerate(string):
        print(f"posicion : {i}, caracter {char}")
imp_char_y_pos("cancamusa")
#La f antes de las comillas en print(f"Posición: {i}, Carácter: {char}") 
#indica que la cadena es una cadena de formato o f-string en Python.

#Las cadenas de formato son una característica de Python que permite insertar 
#expresiones dentro de cadenas literales, usando llaves {}. Las expresiones 
#serán reemplazadas por sus valores.