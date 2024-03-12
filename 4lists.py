# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4lists.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/10 13:11:46 by marvin            #+#    #+#              #
#    Updated: 2024/03/10 13:11:46 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Una lista en python es parecido a lo que conocemos como una matriz en c se declara asi:
lista = ["esto", "es", "una", "lista"]

#METODOS

#1:append(elemento)-> agrega un elemento al final de la lista
lista.append("inteligente")
print(lista) #['esto', 'es', 'una', 'lista', 'inteligente']
#2:extend(iterable)->agrega todos los elementos de un iterable(lista o tupla) al final de la lista
lista.extend(["esto", "es", "añadido"])
print(lista) #['esto', 'es', 'una', 'lista', 'inteligente', 'esto', 'es', 'añadido']
#3:insert(indice, elemento)->inserta un elemento en una posicion especifica de la lista
lista.insert(4, "insertado")
print(lista) #['esto', 'es', 'una', 'lista', 'insertado', 'inteligente', 'esto', 'es', 'añadido']
#4:remove(elemento)->elimina la primera aparicion del elemento en la lista
lista.remove("inteligente")
print(lista) #['esto', 'es', 'una', 'lista', 'insertado', 'esto', 'es', 'añadido'] 
#5:pop(indice)-> elimina y devuelve el elemento en una posicion especifica de la lista
elemento = lista.pop(4)
print(lista)
print(elemento)
#6:index(elemento)->devuelve el indice de la primera aparicion de un elemento en la lista
print(str(lista.index("lista"))) #3
#7:count(elemento)->devuelve el num de veces que un elemento aparece en la lista
print(str(lista.count("es"))) #2
#8:sort()->ordena en ascendente los elemento de la lista
lista.sort()
print(lista) #['añadido', 'es', 'es', 'esto', 'esto', 'lista', 'una']
#9->reverse()->invierte el orden de los elementos de la lista
lista.reverse()
print(lista) #['una', 'lista', 'esto', 'esto', 'es', 'es', 'añadido']
