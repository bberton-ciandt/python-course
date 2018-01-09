imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

title, artist, year, tracks = imelda

print("Title: {}".format(title))
print("Artist: {}".format(artist))
print("Year: {}".format(year))
print("Tracks: ")
for track_number, track_name in tracks:
    print("\t", track_number, track_name)

