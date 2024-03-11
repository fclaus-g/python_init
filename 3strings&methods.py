# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    strings&methods.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/09 18:11:53 by marvin            #+#    #+#              #
#    Updated: 2024/03/09 18:11:53 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#En este archivo vamos a aglutinar funciones con strings y sus métodos para 
#tener mas claros los conceptos
# def printstr(str):
#     print(str)
# printstr("esto es una frase")
# def findword(str, word):
#     if word in str:
#         print(word + " se encuentra en la frase")
# findword("la frase es esta", "esta")

#Algo que me resulta muy util y curioso es el uso de indices en python,
#veamos unos ejemplos:

# str="Hola amigo"
# print(str[0])   #print H
# print(str[:5])  #print Hola
# print(str[5:10])#print amigo
# print(str[5:])  #print amigo
# print(str[-5])  #print a(posicion 5 contando desde el final hacia atras)
# print(str[-5:]) #print amigo
# print(str[:-5]) #print Hola

#Hay que tener en cuenta que una string en python es de caracter inmutable
#lo que quiere decir es que si a una string queremos cambiar un caracter 
#hay que crear una string nueva que lo incluya, por ejemplo:

#METODOS

str  = "  leonardo es un maquina  "
#1:capitalize convierte el primer char de una string en mayuscula
print(str.capitalize()) #  Leonardo es un maquina  
#2:upper-> convierte a mayusculas la string
print(str.upper()) #  LEONARDO ES UN MAQUINA  
#3:lower-> convierte a minusculas la string
print(str.lower()) #  leonardo es un maquina  
#4:strip->elimina los espacios en blanco al principio y al final
print(str.strip()) #leonardo es un maquina
#5:replace-> reemplaza las ocurrencias de la subcadena old con new
print(str.replace("leonardo", "fernando")) #  fernando es un maquina
#6split->divide la cadena en una **lista** de subcadenas con el separador elegido
print(str.split(" ")) #[' ', ' '. 'leonardo', 'es', 'un', 'maquina', ' ', ' ']
#7join(iterable)->Une todos los elementos de un iterable(lista o tupla) en una string
lista = ["leonardo", "es", "un", "maquina"]
print("|".join(lista)) #leonardo|es|un|maquina
#8index-> devuelve la posicion de la subcadena
print(str.index("es")) #11



def cambiar_char(str, c, n):
    new_str = str.replace(c, n)
    print(new_str)
cambiar_char("cancamusa", "c", "k")