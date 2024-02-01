## For this code, you need to have the .txt file
## **IN THE SAME DIRECTORY AS THIS PROGRAM**

## We will learn about how to access files that are
## in a different directory.


## Step one: Make a text file with you playlist.
## Call the file my_playlist.txt.
## You can make the file with TextEdit on Mac or Notepad on Windows.
## Or you can just use IDLE and Save As... to a text file.

# open the file and save it as a file object, f
f = open("my_playlist.txt", "r")

# create an empty list
mylist = []

# for each line in the file...
for line in f:

    # append that line to the list
    # rstrip() chops off the new line
    mylist.append(line.rstrip())

# close the file
f.close()

print(mylist)


# open a file for *writing*
g = open("ratings.txt", "w")

# for every item in the list
for s in mylist:

    # Write that song out to the file.
    # Don't forget that write() takes only a string argument.
    # You have to use + and you need to insert your own newline \n
    g.write(s + " IS THE BEST SONG EVER!!!" + "\n")


g.close()

         

#print(data)
