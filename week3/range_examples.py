## Three different uses of range()
## using factorial as an exampl

n = int(input("integer: "))

# With one argument, range means
# start at 0, increase by 1, and
# stop right before you get to arg1.
nfac = 1
for i in range(n):
    nfac = nfac * (i+1)
print(nfac)

# With two arguments, range means
# start at arg1, increase by 1, and
# stop right before you get to arg2.
nfac = 1
for i in range(1,n+1):
    nfac = nfac * i
print(nfac)

# With two arguments, range means
# start at arg1, increase by arg3 (or
# deacrease is arg3 is negative, and
# stop right before you get to arg2.
nfac = 1
for i in range(n, 0, -1):
    print("i =", i)
    nfac = nfac * i
print(nfac)


## More range() examples...
## Run them to see what they do
for i in range(15, 4, -1):
    print(i)

for i in range(100,-1,-5):
    print(i)

for i in range(0,100,7):
    print(i)
