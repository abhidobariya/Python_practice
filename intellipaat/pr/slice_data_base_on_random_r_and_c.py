import numpy as np

arr1 = np.array((
    [5,10,15],
    [20,25,30],
    [35,40,45],
    [1,2,3],
    [40,50,60]
))
print(arr1)

## [5,10,15]
## [1,2,3]

a= arr1[[0,3]]
print(a)

##random

a= arr1[:,[0,1]]
print(a)

#10,25

a = arr1[0:2,1]
print(a)

##Practice question

## [20,25]
## [40,50]

a =arr1[[1,4],0:2]
print(a)

##[5,10,15]
##[40,50,60]

a =arr1[[0,4],0:3]
print(a)

#or

a= arr1[[0,4]]
print(a)


##[40,45]
##[2,3]

a =arr1[[2,3],1:3]
print(a)

#or

a=arr1[2:4,1:3]
print(a)

##[20,60]

a=arr1[[1,4],[0,2]]
print(a)
