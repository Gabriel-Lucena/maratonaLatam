numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.

# for i in range(length // 2):
# my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# Note:

# we've assigned the length variable with the current list's length(this makes our code a bit clearer and shorter)
# we've launched the for loop to run through its body length // 2 times(this works well for lists with both even and odd lengths, because when the list contains an odd number of elements, the middle one remains untouched)
# we've swapped the ith element(from the beginning of the list) with the one with an index equal to(length - i - 1)(from the end of the list)
# in our example, for i equal to 0 the(length - i - 1) gives 4
# for i equal to 1, it gives 3 ‒ this is exactly what we needed.
