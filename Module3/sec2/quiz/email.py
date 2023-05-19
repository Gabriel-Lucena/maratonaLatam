x = ""

for char in "john.smith@pythoninstitute.org":

    if char == "@":
        break

    x = x + char


print(x)
