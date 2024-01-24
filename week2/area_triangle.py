# calculate the area of a triangle

def area_triangle(b, h):
    area = .5 * b * h
    print(area)

# Here are lots of different ways to call the function
def main():

    # using actual numbers
    area_triangle(2,4)
    area_triangle(11,4)

    # creating variables and giving those as arguments
    # it doesn't matter what you call those variables!

    base = 2
    height = 5
    area_triangle(base, height)

    b = 7
    h = 3
    area_triangle(b, h)


    x = 10
    y = 2
    area_triangle(x,y)


main()
