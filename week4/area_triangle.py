# Two different versions of the are of a triangle function.

# This one *prints* the area.
def tri_area_print(h,b):
    area = (b*h)/2
    print(area)

# This one *returns* the area.
def tri_area_return(h,b):
    area = (b*h)/2
    return(area)


h1 = 5
b1 = 4

h2 = 6
b2 = 3

tri_area_print(h1, b1)
tri_area_print(h2, b2)

a1 = tri_area_return(h1,b1)
a2 = tri_area_return(h2,b2)


if a1 > a2:
    print(f"The area of the triangle with b={b1} and h={h1}" +
            f"is larger than the triangle with b={b2} and h={h2}")
else:
    print(f"The area of the triangle with b={b2} and h={h2}" +
            f"is larger than the triangle with b={b1} and h={h1}")
