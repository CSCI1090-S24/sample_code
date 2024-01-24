name="Amit"
year=2026
major="History"

# Print just by giving arguments separated by space
# Python will automatically insert a space between each one
print(name, "|||", year, "|||", major)

# Tell Python to use " ||| " as the separator instead of space
print(name, year, major, sep=' ||| ')

# Concatenate strings with +
print(name + " ||| " + str(year) + " ||| " + major)

# using f-strings
print(f"{name} ||| {year} ||| {major}")


# Rememember, print() inserts a new line after each print statement.
# You can suppress that using the end argument.

print(name + " ||| ", end="")
print(str(year) + " ||| ", end="")
print(major)
