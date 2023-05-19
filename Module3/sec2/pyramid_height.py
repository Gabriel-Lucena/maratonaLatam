blocks = float(input())
i = 0
sumBlocks = 0

while sumBlocks != blocks:

    i = i + 1
    sumBlocks = sumBlocks + i;

    if sumBlocks > blocks:
        i = i - 1
        break

print("The height of the pyramid:", i)
