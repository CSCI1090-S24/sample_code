# Function that returns two things!
def sumprod(a, b):
    summy = a+b
    prod = a*b
    return summy, prod

# What is it returning? A tuple! 

# You can call it like this, where you specify each of the
# things it returns as its own variable
s, p = sumprod(0,10)
print(s, p)

# Or you can call it like this, where you save what it returns to
# a single variable that's a tuple. Then you can access them
# elements in the tuple with brackets and indices.
mytuple = sumprod(0, 10)
print(mytuple[0], mytuple[1])

# Here's something you can do with the output.
if s > p:
    print(f"The sum {s} is greater than the product {p}")
else:
    print(f"The sum {s} is less than the product {p}")
    
