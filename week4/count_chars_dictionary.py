mytext = "Taylor Swift made history, taking home Album of \
        the Year for Midnights, her fourth win in the category. \
        Miley Cyrus brought down the house with her performance\
        of Flowers, two hours before winning Record of the Year. \
        Victoria Monét was crowned Best New Artist while Billie \
        Eilish and Finneas's What Was I Made For, from the Barbie \
        soundtrack, won Song of the Year."

# Create empty dictionary
charcount = {}

# for every character in the text...
for c in mytext:

    # if it exists, add one
    # otherwise set it to 0 then add one
    charcount[c] = charcount.get(c, 0) + 1


# alternative with if/else

# Create empty dictionary
charcount = {}

# for each character in the text...
for c in mytext:

    # check to see if it's in the dictionary.
    # if it is, add one
    if c in charcount:
        charcount[c] += 1

    # otherwise set the value for that key to 1
    else:
        charcount[c] = 1

# how many unique characters
print(charcount)

# print out count of "e"
print(f"the count of 'e' is {charcount['e']}")

# better: check to make sure it's in there first!
if "z" in charcount:
    print(f"the count of 'z' is {charcount['z']}")
else:
    print(f"the count of 'z' is 0")


# and here's how to do that with less code
print(f"the count of 'q' is {charcount.get('z', 0)}")

