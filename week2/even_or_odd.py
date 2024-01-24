
# Function that tells you when the int parameter
# is even or odd using the mod operator.

def even_or_odd(n):

    # if the remainder after dividing by 2 is 0, it's even!
    if n%2 == 0: 
        print(n, "is even!")

    # otherwise, it's odd
    else:
        print(n, "is odd!")

# giving an integer as the argument
even_or_odd(11)

# giving a variable that's an integer as the argument
c = 12
even_or_odd(c)
