# Version 1: compare letters from either end.
# Change from True to False when you find a mismatch.
def palindrome(s):
    start = -1
    palind = True
    for c in s:
        if c != s[start]:            
            palind = False
        start = start - 1
    return palind


# Version 2: make a backwards version of the string.
# Check if the backwards and forwards version are the same.
# If so, return true. Otherwise return false.
def palindrome2(s):
    sbackwards = s[::-1]
    if sbackwards == s:
        return True
    else:
        return False

# Version 3: make a backwards version of the stirng.
# Return whether they are the same (which will be True or False).
def palindrome3(s):
    sbackwards = s[::-1]
    return sbackwards == s


# Version 4: compare letters from either end.
# RETURN when you find a mismatch.
def palindrome(s):
    start = -1
    for c in s:
        if c != s[start]:            
            return False
        start = start - 1
    return True


# Example of how to use the function.
yourword = input("word: ")
if palindrome(yourword) == True:
    print(f"{yourword} is a palindrome")
else:
    print(f"{yourword} is NOT a palindrome")


# Print how many words in a list are palidromes.
listofwords = ["anna", "racecar", "elephant", "tacocat", "chair"]
howmanypalindromes = 0

for w in listofwords:
    if palindrome3(w) == True:
        howmanypalindromes += 1

print(f"Of the {len(listofwords)} words, {howmanypalindromes} were palindromes")

