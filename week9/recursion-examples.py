# iterative function to get string length
def string_length(s):
    length = 0
    for w in s:
        length += 1
    return length

# another iterative function to get string length
def string_length2(s):
    length= 0
    while s != "":
        s = s[1:]
        length += 1
    return length

# recursive  function to get string length
def string_recursive(s):
    if s == "":
        return 0
    return 1 + string_recursive(s[1:])

print(string_length("emily"))
print(string_length2("emily"))
print(string_recursive("emily"))



##################

# iterative function to calculate factorial
def factorial_iterative(n):
    total = 1
    while n != 0:
        total = total * n
        n = n-1
    return total

# recursive function to calculate factorial
def factorial_recursive(n):
    print(f"n is currently {n}")
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(6))
print(factorial_recursive(6))



##################

# iterative function to reverse a string
def reverse(s):
    s2 = ""
    for i in range(len(s)-1, -1, -1):
        s2 = s2 + s[i]
    return s2

# another iterative function to reverse a string
def reverse2(s):
    s2 = ""
    while s != "":
        s2 = s[0] + s2
        s = s[1:]
    return s2


# recursive function to reverse a string
def reverse_recursive(s):
    if s == "":
        return s
    return reverse_recursive(s[1:]) + s[0]


print(reverse("computer"))
print(reverse2("computer"))
print(reverse_recursive("computer"))



#############

# recursive sequential (linear) search
def sequential_recursive(guess, target):
    if guess == target:
        print(f"You guessed the number {target} in {guess} guesses!")
        return
    sequential_recursive(guess+1, target)


# recursive binary search
def binary_recursive(lo, hi, target, guesses):
    mid = (hi+lo) // 2
    if mid == target:
        print(f"You guessed the number {target} in {guesses} guesses!")
        return
    if mid < target:
        binary_recursive(mid+1, hi, target, guesses+1)
    else:
        binary_recursive(lo, mid-1, target, guesses+1)


number_to_guess = 29
sequential_recursive(1, number_to_guess)
binary_recursive(1, 30, number_to_guess, 1)


