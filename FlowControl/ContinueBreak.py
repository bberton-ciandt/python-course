shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy {}".format(item))

nasty_food_item = None
for item in shopping_list:
    if item == "spam":
        nasty_food_item = item
        break
else:  # this will be executed if the for finishes without a break
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it?")
