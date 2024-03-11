# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bucles.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/09 20:11:00 by marvin            #+#    #+#              #
#    Updated: 2024/03/09 20:11:00 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#algunos ejemplos de bucles while para mejorar la comprensión y el uso.

#WHILE
def print_num_veces(iteraciones):
    x = 0
    while x < iteraciones:
        print("imprimimos" + str(x + 1) + "veces")
        x += 1
    print("terminado")
print_num_veces(4)

def tabla_de_multiplicar(num):
    x = 0
    if num > 0:
        while x <= 10:
            print(str(num) + '*' + str(x) + '=' + str(num * x))
            x += 1    
    else:
        print ("el 0 no vale titi")
    print("listo")
tabla_de_multiplicar(0)

def fizzbuzz():
    x = 0
    while x <= 100:
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 5 == 0:
            print("buzz")
        elif x % 3 == 0:
            print("fizz")
        else:
            print(str(x))
        x += 1
fizzbuzz()   