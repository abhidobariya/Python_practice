import numpy as np

arr_2d = np.array((

[5,10,15],
[20,25,30],
[35,40,45]

))

print(arr_2d)

## access element 40

a = arr_2d[2,1]
print(a)

## acces element 30
a = arr_2d[1,2]
print(a)

## acces element 25
a = arr_2d[1,1]
print(a)

## acces element 35
a = arr_2d[2,0]
print(a)
                                                   # 5 10 15
## acces element # 10 15                           # 20 25 30
                 # 25 30                           # 35 40 45

a = arr_2d[0:2,1:3]
print(a)

## acces element 20, 25, 30
a = arr_2d[1:2,0:3]
print(a)


## acces element #5 ,10
                 #20, 25
a = arr_2d[0:2,0:2]
print(a)

## acces element #20, 25, 30
                 #35, 40, 45

a = arr_2d[1:3,0:3]
print(a)

