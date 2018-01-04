age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}".format(31, "January", "March", "May"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}""".format(28, 30, 31))

###########################################################################
# this is deprecated in python3
# this is used in python 2.7
###########################################################################
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("Pi is approximately %12.50f" % (22/7))
###########################################################################

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.51}".format(22/7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
