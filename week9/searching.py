import random

# LINEAR SEARCH
# Just start at 1 and keep guessing
def linear_search(n):
    guesses = 1
    while guesses != n:
        guesses += 1
    return guesses


# NAIVE RANDOM SEARCH
# randomly guess numbers in the range
# duplicates allowed!
def random_naive(n):
    guesses = 1
    thisguess = random.randint(1, 15)
    while thisguess != n:
        thisguess = random.randint(1, 15)
        guesses += 1
    return guesses


# SMARTER RANDOM SEARCH
# take all the numbers in the range
# shuffle them, then guess them one by one
# no duplicates allowed
def random_smarter(n):
    guesses = 0
    numbers = list(range(1,16))
    random.shuffle(numbers)

    while numbers[guesses] != n:
        guesses += 1

    return guesses


# BINARY SEARCH
def binary_search(n):
    
    guesses = 1

    # top, bottom, and middle of the current range
    lo = 1
    hi = 15
    mid = (hi+lo) // 2

    # if the middle (your guess is not correct...)
    while mid != n:

        # if it's too big, lower the top of the range
        if mid > n:
            hi = mid - 1

        # otherwise, increase the bottom of the range
        else:
            lo = mid + 1
        mid = (hi+lo) // 2
        
        guesses += 1
    return guesses


thenumber = random.randint(1, 15)
print(f"Trying to guess {thenumber}")
print(f"Linear took {linear_search(thenumber)} guesses")
print(f"Random naive took {random_naive(thenumber)} guesses")
print(f"Random smarter took {random_smarter(thenumber)} guesses")
print(f"Binary took {binary_search(thenumber)} guesses")

