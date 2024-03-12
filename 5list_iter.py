# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    5list_iter.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/11 18:01:16 by marvin            #+#    #+#              #
#    Updated: 2024/03/11 18:01:16 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Aquí vamos a ver el uso de iteraciones en las listas y sus particularidades

lista_colegas = ["alberto", "tino", "juanma", "fernando"]
print(lista_colegas) #["alberto", "tino", "juanma", "fernando"]
num_char = 0
for colega in lista_colegas: #colega es un contador que ca pasando por la lista y toma el valor de cada elemnto en la iteracion
   num_char += len(colega) #num_char = al numero de char del largo de cada elemento
print("Total char: {}, longitud media: {}".format(num_char, num_char/len(lista_colegas)))
#Total char: 25, longitud media: 6.25
##**format** es un metodo que se usa para dar formato a una cadena insertando valores en ella
#en lugar del uso de "+" permite añadir variables a la string mediante llaves e invocando a
#format(variable1, variable2). Seria como printf en C, siendo {} == %x ejemplo:
variable1 = "hola"
variable2 = "ea"
print("Aqui entrara la {}, y aqui la: {}".format(variable1, variable2))
#Aqui entrara la hola, y aqui la: ea 
#es similar a printf("Aqui entrara la %s, y aqui la: %s", variable1, variable2)

# **enumerate()**->devuelve una tupla que contiene un contador (que comienza en 0 por defecto)
# y el valor del elemento correspondiente en la lista. Estos valores se desempaquetan en las 
#variables index y persona, respectivamente.

for index, persona in enumerate(lista_colegas):
   print("orden de lectura {}- {}".format(index, persona))
# orden de lectura 0- alberto
# orden de lectura 1- tino
# orden de lectura 2- juanma
# orden de lectura 3- fernando 


def emails(personas):
    result = []
    for email, nombre in personas:
       result.append("{} <{}>". format(nombre, email))
    return(result)
print(emails([("paco@tusmulas", "paco pepe"), ("pepe@tusriles", "pepe Paco")]))

def convertir_segundos(segundos):
   horas = segundos // 3600 #el operador // devuelve un int en lugar de un float
   print("horas = " + str(horas))
   minutos = (segundos - horas * 3600) // 60
   print ("minutos = " + str(minutos))
   segundos_sobrantes = segundos - horas * 3600 - minutos * 60
   print("segundos = " + str(segundos_sobrantes))
   return horas, minutos, segundos_sobrantes
# al retornar varios valores result se convierte en una tupla   
result = (convertir_segundos(23250))
print("resultado = " + str(result) + str(type(result)))
# horas = 6
# minutos = 27
# segundos = 30
# resultado = (6, 27, 30)<class 'tuple'>
car_make = "Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])