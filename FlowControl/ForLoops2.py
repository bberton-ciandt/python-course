number = "9,223,372,036,854,775,807"
cleaned_number = ''

for char in number:
    if char in '0123456789':
        cleaned_number = cleaned_number + char

new_number = int(cleaned_number)
print("The number is {}".format(new_number))

for state in ["not pining'", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i * j))
    print("================")
