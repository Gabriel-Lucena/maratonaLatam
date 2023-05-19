integer = int(input())
contador = 0

while integer != 1:

    if integer % 2 == 0:

        integer = integer / 2
        print(integer)

    else:

        integer = 3 * integer + 1
        print(integer)

    contador = contador + 1

print(contador)
