my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    for j in my_list[i:]:
        if i == j:
            del my_list[j]

my_list.sort()

print("The list with unique elements only:")
print(my_list)
