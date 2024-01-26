# Which number is smaller or are they the same?
# Note the use of elif !

def smaller(a,b):
    if a < b:
        print(a, "is smaller than", b)
    elif(b<a):
        print(b, "is smaller than", a)
    else:
        print(a, "is equal to", b)

smaller(10, 10)

