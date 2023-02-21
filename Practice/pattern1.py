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