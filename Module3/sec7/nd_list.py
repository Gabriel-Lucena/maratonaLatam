temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)


# 3 dimensions

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Check if there are any vacancies on the 15th floor of the third building:

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
