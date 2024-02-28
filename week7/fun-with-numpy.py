import numpy as np

# read in just the grades
grades = np.loadtxt("pretendgrades.csv",
                     delimiter=",",
                     skiprows=1,
                     usecols=(1, 2, 3, 4, 5, 6),
                     dtype=int)

# read in just the names of the students
people = np.loadtxt("pretendgrades.csv",
                     delimiter=",",
                     skiprows=1,
                     usecols=(0),
                     dtype=str)

# print out everyone and their grades
for i in range(len(people)):
    gradeslist = grades[i].tolist()
    print(f"{people[i]}:{" "*(10-len(people[i]))} {gradeslist}")

print()

# axis=0 looks vertically at columns: for each quiz, which student
# did the best
top_student = people[np.argmax(list(grades), axis=0)]

for i in range(len(top_student)):
    print(f"{top_student[i]} got the highest grade on Quiz {i+1}")

print()

# axis = 1 looks horizontally at rows: for each student, which quiz
# was their highest score
best_quiz = np.argmax(list(grades), axis=1)

for i in range(len(best_quiz)):
    print(f"{people[i]} did best on Quiz {best_quiz[i]+1}")




# mean and standard deviation on each quiz
means = np.mean(grades, axis=0)
stdevs = np.std(grades, axis=0)

for i in range(len(means)):
    print(f"Quiz {i+1}: mean={means[i]:.2f}, stdev={stdevs[i]:.3f}")


# person with lowest grade on each quiz
student = people[np.argmin(list(grades), axis=0)]

for i in range(len(student)):
    print(f"{student[i]} got the lowest grade on Quiz {i+1}")


# lowest and highest for each student
min_grades = np.min(grades, axis=1)
max_grades = np.max(grades, axis=1)

for i in range(len(people)):
    print(f"{people[i]}: min={min_grades[i]}, max={max_grades[i]}")
