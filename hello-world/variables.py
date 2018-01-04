a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
# print as a float by default
print(a / b)
# print as an integer
print(a // b)
print(a % b)

for i in range(1, a // b):
    print(i)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:9])
print(parrot[:9])
print(parrot[9:])
print(parrot[-4:])

number = "9,223,372,036,854,775,807"
print(number[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

string1 = "he's "
string2 = "probably"
print(string1 + string2)
print("he's " "probably " "pining")

print("Hello " * 5)
print("Hello " * (5 + 4))

today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")
