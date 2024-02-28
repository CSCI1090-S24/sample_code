show1 = ["David", "Alexis", "Moira", "Johnny"]
show2 = ["Walter", "Jesse", "Skyler", "Saul"]
show3 = ["Elizabeth", "Diana", "Margaret", "Queen Mum"]

allshows = show1 + show2 + show3
print(allshows)
print(allshows[1])

allshows = [show1, show2, show3]
print(allshows)
print(allshows[2][2])

x = [ [ [0,0], [0,0] ],
      [ [1,1], [1,1] ],
      [ [2,2], [2,2] ] ]

x[1][0][1] = 8

for i in x:
    print(i)
    for j in i:
        print("\t", j)
        for k in j:
            print("\t\t", k)
