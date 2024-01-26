# Wish someone happy birthday as many times as they like.
# Use a while loop or a for loop!


numbday = int(input("How many times? "))

# Repeating something with a while loop

# create a counter variable outside the loop
i = 0

# while that counter variable is less than the target
while i < numbday:

    # print the message
    print("Happy Birthday!")

    # add one to the counter variable
    # (Comment this out to get an infinite loop!)
    i = i+1

print()


# Repeating something with a for loop
numbday = int(input("How many times? "))

# Advantages of for loop:
# * You don't need to set the counter variable
# * You don't need to increment the counter variable

for i in range(numbday):
    print("Happy Birthday!")

# Range is a function that gives you a sequence of numbers
# start at zero and going up to (but not including) the number
# inside the parentheses.
