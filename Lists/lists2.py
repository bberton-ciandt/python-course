list1 = []
list2 = list()

if list1 == list2:
    print("The lists are equal")

print(list("The lists are equal"))

even = [2, 4, 6, 8]

# another_even = even this will make another_even to be the same instance as even
another_even = list(even)  # this will make another_even to be a different instance of even
another_even = sorted(even, reverse=True) # this will make another_even to be a different instance of even too

print(another_even is even)

another_even.sort(reverse=True)
print(even)
print(another_even)


odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
print(numbers)

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)
