def message():
    print("Enter a value: ")
    integer = int(input())

    return integer


def media(x, y): return (x + y) / 2


a = message()
b = message()
c = message()

print(a, b, media(a, b), c)
