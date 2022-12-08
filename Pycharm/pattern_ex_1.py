# 1
# 12
# 123
# 1234
# 12345

# rows= 5
#
# for i in  range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print("")


# 1
# 22
# 333
# 4444
# 55555

# rows=6
#
# for i in range(rows):
#     for j in range(i):
#         print(i,end='')
#     print("")

# 11111
# 2222
# 333
# 44
# 5

# rows= 5
# b = 0
# for i in range(rows,0,-1):
#     b += 1
#     for j in range(1,i+1):
#         print(b,end='')
#     print("")

# 55555
# 4444
# 333
# 22
# 1

# rows= 5
#
# for i in range(rows,0,-1):
#     # num = i
#     for j in range(0,i):
#         print(i,end='')
#     print("")

#     1
#    22
#   333
#  4444
# 55555

rows = 5

for i in range(rows+1):

    for j in range(0,i):
        print("*",end='')
    print("")