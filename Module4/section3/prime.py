def is_prime(num):
    i, contador = 1, 0

    while i <= num:

        if num % i == 0:
            contador += 1

        i += 1

    if contador == 2:

        return True

    else:

        return False


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
