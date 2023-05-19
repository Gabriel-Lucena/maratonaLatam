row = []

for i in range(8):
    row.append(WHITE_PAWN)

row = [WHITE_PAWN for i in range(8)]

# x ** 2

squares = [x ** 2 for x in range(10)]

# 2 ** n

twos = [2 ** i for i in range(8)]


cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]
