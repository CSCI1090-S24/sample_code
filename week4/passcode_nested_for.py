# You have a three letter passcode but you forgot it!
# You know the letters include A, B, C, or D.
# Here's how you would use brute force to try to
# crack the code (i.e., to come up with every possibility).

letters = "ABCD"

passcode = ""

for a in letters:
    #print("\nWORKING ON FIRST LETTER: ", a)

    for b in letters:
        #print("WORKING ON SECOND LETTER: ", b)

        for c in letters:
            passcode = a+b+c
            print(passcode)

