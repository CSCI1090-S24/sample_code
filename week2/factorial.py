n = int(input("Enter a number: "))

# set a variable to store the result
# set it to 1 since we're going to multiply
fac = 1

# Use a for loop
for i in range(5):
    print("i =", i)
    print("fac =", fac)
    fac = fac * (i+1)
    print("now fac =", fac)
    print()

print(n, "! = ", fac, sep="")
