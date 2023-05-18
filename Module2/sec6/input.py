# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")

# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# Testing a TypeError message.

# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", round(hypo, 5))

# Força a ser

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
