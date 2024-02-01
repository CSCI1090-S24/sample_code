def pos_neg_zero(n):
    if n > 0:
        print(n, "is positive")
    elif n == 0:
        print(n, "is zero!")
    else:
        print(n, "is negative")


pos_neg_zero(-7)
pos_neg_zero(0)

## this will give an error.
## why? because n is only visible inside the function, abovew
print(n)










