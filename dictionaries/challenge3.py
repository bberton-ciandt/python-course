vowels = frozenset("aeiou")
# vowels = {"a", "e", "i", "o", "u"}
print(vowels)

my_text = input("Type some text: ")

my_text_set = set(my_text)

print(sorted(list(my_text_set.difference(vowels))))
