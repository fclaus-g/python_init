# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    6compresiones                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/11 19:40:49 by marvin            #+#    #+#              #
#    Updated: 2024/03/11 19:40:49 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#entiendo que la traduccion de comprehesiones en ingles es compresiones, del verbo
#comprimir porque es de lo que va esta movida:
multiplos = []
for x in range(1, 11):
    multiplos.append(x*7)
print(multiplos)
#[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
multiplos = [x*7 for x in range(1, 11)]
print(multiplos)
#[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#A fin de cuentas es meter en una sola linea varias movidas

lenguajes = ["python", "C", "C++", "Rust"]
len = [len(lenguaje) for lenguaje in lenguajes]
print(len)
#[6, 1, 3, 4]

multiplos = [x for x in range(1, 33) if x % 3 == 0]
print(multiplos)
#[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

#como hemos visto cabe perfectamente un bucle y una condición