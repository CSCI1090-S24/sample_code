## Three different ways to go through a string and
## print out the letters one per line

# use for i in range()
def print_letters(s1):
    for i in range(len(s1)):
        print(s1[i])

# use while loop
def print_letters2(s1):
     i =0
     while i < len(s1):
         print(s1[i])
         i = i+1

# use for character in sting
def print_letters3(s1):
    for c in s1:
        print(c)

print_letters3("Hello!")
print_letters2("Hello!")
print_letters3("Hello!")


## Two different ways to print out what letters
## in one string are in another string

# use for character in string
def compare_strings(s1, s2):
    for c in s1:
        if c in s2:
            print(c, "is in", s1, "and", s2)

# use for i in range()
def compare_strings2(s1, s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            print(s1[i], "is in", s1, "and", s2)



compare_strings("alligator", "aardvark")
compare_strings2("elephant", "ant")
