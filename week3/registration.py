year = input("what year? ")
major = input("CS major (Y/N): ")


## Using the and operator
priority = 0

if year == "senior" and major == "Y":
    priority = 1
elif year == "junior" and major == "Y":
    priority = 2
elif year == "senior":
    priority = 3
elif year == "sophomore" and major == "Y":
    priority = 4
elif year == "junior":
    priority = 5
else:
    priority = 6
    
    
print(priority)


# using nested for loops
if year == "senior":
    if major == "Y":
        priority = 1
    else:
        priority = 3
elif year == "junior":
    if major == "Y":
        priority = 2
    else:
        priority = 5
elif year == "sophomore":
    if major == "Y":
        priority = 4
else:
    priority = 6

print(priority)
