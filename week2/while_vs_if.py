

# While loops and if statements both use conditions
# but while loops keep executing code until the condition
# is no longer true.
n = int(input("Enter an even number: "))

while n%2 != 0:
    n = int(input("Enter an even number: "))

print("Thank you for finally entering an even number:", n)


# If statements excute their code block only once
# if the condition is met.

print("~~~~~~~", "STARTING OVER WITH IF", "~~~~~~", sep="\n")

n = int(input("Enter an even number: "))

if n%2 != 0:
    n = int(input("Enter an even number: "))

print("Thank you for finally entering an even number:", n)










    











    

