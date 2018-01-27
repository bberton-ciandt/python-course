fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# fruit["pear"] = "great with tequila"
# print(fruit)
#
# del (fruit["lemon"])
# print(fruit)
#
# fruit.pop("grape")
# print(fruit)
#
# fruit.clear()
# print(fruit)

print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("Don't have a " + dict_key)

for snack in fruit:
    print(fruit[snack])
