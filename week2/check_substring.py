# check if a is a substring of b
# or if b is a substring of a
# or neither

def substring(a, b):
    if a in b:
        print(a, "is a substring of", b)
    elif b in a:
        print(b, "is a substring of", a)
    else:
        print("neither is a substring of the other")

substring("elephant", "dog")
substring("elephant", "ant")
substring("ant", "elephant")

