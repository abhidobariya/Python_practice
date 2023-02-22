# *
# * *
# * * *
# * * * *

a=4

for i in range(0,a):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")


# 1
# 1 2
# 1 2 3
# 1 2 3 4


a = 5
for i in range(0,a):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")


# 1
# 2 2
# 3 3 3
# 4 4 4 4

a=5

for i in range(0,a):
    for j in range(i):
        print(i,end=" ")
    print("\r")




# 1 1 1 1
# 2 2 2
# 3 3
# 4

a = 5

for i in range(1,a):
    for j in range(i,5):
        print(i,end=" ")
    print("\r")


#       1
#     2 2
#   3 3 3
# 4 4 4 4

a=5
for i in range(1,a):
    for j in range(i,0,-1):
        print(i,end=" ")
    print("\r")



# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

a = 6

for i in range(1,a):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\r")


# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

a = 6

for i in range(a,0,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print("\r")



# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

a = 5

for i in range(a,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print("\r")



# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5


a= 6
for i in range(a,0,-1):
    for j in range(i,a):
        print(j,end=" ")
    print("\r")