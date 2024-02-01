## create lists of songs
taylor = ["Bad Blood", "22", "Shake It Off", "Blank Space"]
beatles = ["Hey Jude", "Revolution", "Mean Mister Mustard", "Help"]

# combine those two lists into one big list
allsongs = taylor+beatles

# print out the length of all three lists
print(len(taylor))
print(len(beatles))
print(len(allsongs))

# Go through that list and print out each song
# separated by comma. This will, unfortunately,
# print out a comma after the last song.

for s in allsongs:
    print(s, end = ", ")
print()


## This will avoid that. You have to use range()!
for i in range(len(allsongs)-1):
    print(allsongs[i], end=", ")
print(allsongs[-1])


## This is probably the easiest way, though!
## We'll learn more about join() soon.
print(", ".join(allsongs))
