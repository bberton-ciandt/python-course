string = "1234567890"

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for char in string:
    print(char)

for char in iter(string):
    print(char)


my_list = [1, 11, 111, 1111, 11111, 111111]
my_list_iterator = iter(my_list)
for i in range(0, len(my_list)):
    print(next(my_list_iterator))

for i in my_list:
    print(i)
