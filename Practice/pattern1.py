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

# a
# a b
# a b c
# a b c d

a= 4

for i in range(0,a+1):
    a = 97
    for j in range(1,i+1):
        print("%c"%(a),end=" ")
        a += 1
    print("\r")


# A
# A B
# A B C
# A B C D

a = 4

for i in range(0,a+1):
    A = 65
    for j in range(1,i+1):
        print("%c"%(A),end=" ")
        A += 1
    print("\r")


# a
# b a
# c b a
# d c b a

for i in range(97,101):
    for j in range(i,96,-1):
        print(chr(j),end=" ")
    print()


# A
# B A
# C B A
# D C B A

for i in range(65,69):
    for j in range(i,64,-1):
        print(chr(j),end=" ")
    print("\r")


# 1
# 2 2
# 3 3 3
# 4 4 4 4

a = 5

for i in range(1,a):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\r")


# 4
# 3 3
# 2 2 2
# 1 1 1 1

a = 4

for i in range(a):
    for j in range(i+1):
        print(a-i,end=" ")
    print("\r")


