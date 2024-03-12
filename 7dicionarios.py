# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    7dicionarios.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/12 10:57:12 by marvin            #+#    #+#              #
#    Updated: 2024/03/12 10:57:12 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Aqui veremos lo que son los diccionarios : una struct que almacena pares de
#clave-valor, pudiendo acceder al valor usando la clave. Características mas importantes:
#1->Mantienen el orden de inserción(los elementos se devuelven en el orden en que se insertaron)
#2->Las claves deben ser únicas, si agregas un elemento con una clave que ya existe
#se sobreescribe el valor que tenga.
#3->Los diccionarios son mutables lo que significa que puedes agregar, eliminar y cambiar elementos.
#4->Las claves pueden ser cualquier tipo inmutable, números, cadenas o tuplas.

diccionario = {"nombre":"Fernando", "edad": 40, "ciudad":"Alhaurín"}
#Se puede acceder a los valores usando como indice la clave
print(diccionario["nombre"]) #Fernando

#MÉTODOS
#1->get(key, default) devuelve el valor de una clave si existe en el diccionario
print(diccionario.get("nombre"))  # Fernando
#2->keys() devuelve una vista de todas las claves en el diccionario
print(diccionario.keys())  # dict_keys(['nombre', 'edad', 'ciudad'])
#3->values() devuelve una lista de todos los valores en el dicconario
print(diccionario.values())  # dict_values(['Fernando', 40, 'Alhaurín'])
#4->items() devuelve una vista de todos los pares clave-valor.
print(diccionario.items())  # dict_items([('nombre', 'Fernando'), ('edad', 40), ('ciudad', 'Alhaurín')])
#5->update(other) actualiza el diccionario con los pares clave-valor de otro, sobreescribiendo si existen
diccionario.update({"pais": "España"})
print(diccionario)  # {'nombre': 'Fernando', 'edad': 40, 'ciudad': 'Alhaurín', 'pais': 'España'}
#6->pop(key, default) elimina la clave del diccionario y devuelve su valor
print(diccionario.pop("edad"))  # 40
#7->popitem() elimina y devuelve un par clave valor del diccionario. En orden LIFO(último en entrar, primero en salir).
print(diccionario.popitem())  # ('pais', 'España')
print(diccionario)  # {'nombre': 'Fernando', 'ciudad': 'Alhaurín'}
#8->clear() elimina todos los elementos del diccionario.
diccionario.clear()
print(diccionario)  # {}