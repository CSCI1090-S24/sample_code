names = ["Bob", "Martha", "Elaine", "Suzanne"]

# Create variables outside your for loop to store
# the max length and name so far.

# NOTE: I initialied maxlength to 0 since I know that is 
# minimum value for length of a string, but you need
# to pick a value for yoru particular problem based on what you
# know about the possible outcomes.
maxlength = 0
maxname = ""

# Go through the list of names
for n in names:

    # Print out the current state of affairs
    print(f"{maxname} is the longest name *so far* with {maxlength} chars")

    # Check the length of the new name. If it's longer, then
    # reset maxlength to that length and maxname to that name
    if len(n) >= maxlength:
        maxlength = len(n)
        maxname = n

print(f"{maxname} is the longest name with {maxlength} chars")
