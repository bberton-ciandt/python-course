t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)
print(metallica[0])

imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

title, artist, year = imelda  # unpacking the tuple
print(title)
print(artist)
print(year)

a = b = c = d = 12
print(a, b, c, d)
a, b = 13, 14
print(a, b)

a, b = b, a
print(a, b)

print('=' * 50)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")


print(imelda)
title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

