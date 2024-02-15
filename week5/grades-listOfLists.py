# This is your list of lists, where you will store the data.
# This is like the stats variable in PS5.
grades = []

## This is where we can store the students' names
names = []

## Read in the grades from a CSV file
## We will be learning the *right* way to do this in a few weeks!

# open the file for reading
f = open("pretendgrades.csv", encoding="utf-8")

# throw out the header line
f.readline()  

# for every line, split it on comma
for line in f:
    data = line.rstrip().split(",")

    # convert each data point from a string to an int
    for i in range(1,len(data)):
        data[i] = int(data[i])

    # print it out so you can see what it looks like
    print(data)

    # append the student's name to the list of names
    names.append(data[0])

    # append the list (minus the name) to your big LoL
    grades.append(data[1:])

f.close()

# print out the LoL to make sure it's a LoL!
print(grades)

print()

# calculate each student's average
# each row is a student
for i in range(len(grades)):
    row = grades[i]
    print(f"{names[i]}'s average = {(sum(row) / len(row)):.2f}")

# Get the averages for the first two quizzes

# create accumulator variables
q1 = 0
q2 = 0

# for each row in the LoL...
for row in grades:

    # add to the running totals for the Q1 (index 0) and Q2 (index 1)
    q1 += row[0]
    q2 += row[1]



print()
print(f"The average for Quiz 1 was: {q1/len(grades):.2f}")
print(f"The average for Quiz 2 was: {q2/len(grades):.2f}")
