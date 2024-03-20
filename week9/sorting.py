import random 

# Here's bubble sort where it keeps bubbling
# even after the list is sorted.
def bubble(mylist):
    for i in range(len(mylist)-1):

        # print(mylist)

        for j in range(len(mylist)-1):
            
            if mylist[j] > mylist[j+1]:

                # swap
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp

    print(mylist)


# Here's bubble sort where it returns when
# the list is sorted (i.e., there are no swaps)
def bubble_check(mylist):
    for i in range(len(mylist)-1):
        swaps = 0

        # print(mylist)

        for j in range(len(mylist)-1):
            if mylist[j] > mylist[j+1]:

                # swap
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
                swaps += 1
        if swaps == 0:
            print(mylist)
            return



def selection(mylist):
    for i in range(len(mylist)):

        # print(mylist)


        # to keep track of current minimum
        # and the index of that minimum
        minval = mylist[i]
        minidx = i

        # compare each element to the minimum
        # if it's small, reset the min to that
        for j in range(i+1, len(mylist)):
            if mylist[j] < minval:
                minval = mylist[j]
                minidx = j

        # swap
        temp = mylist[i]
        mylist[i] = mylist[minidx]
        mylist[minidx] = temp

    print(mylist)



randomlist = [16, 6, 13, 22, 2, 17, 23, 20, 9, 15]
bubble(randomlist)                

randomlist = [16, 6, 13, 22, 2, 17, 23, 20, 9, 15]
bubble_check(randomlist)                

randomlist = [16, 6, 13, 22, 2, 17, 23, 20, 9, 15]
selection(randomlist)                
