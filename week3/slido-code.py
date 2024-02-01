## more practice with I/O that I showed you
## in the Slido quiz

f = open("lunch-options.txt")

for line in f:
    print("Options: ", line)

f.close()



food = ["apple", "Goldfish", "bread", "cookies"]

g = open("todays-lunch.txt", "w")
for f in food:
    g.write(f + "\n")
g.close()

    

with open("lunch-options.txt") as f:

    for line in f:
        print("Options: ", line)


