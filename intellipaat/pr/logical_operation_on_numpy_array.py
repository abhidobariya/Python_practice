import numpy as np

arr1= np.arange(10)
print(arr1)

a=arr1<5
print(a)

a= arr1[arr1<5]
print(a)

a= arr1[arr1>8]
print(a)

a= arr1[arr1==5]
print(a)

a= arr1[arr1!=5]
print(a)

a= arr1[(arr1!=5)&(arr1>5)]  ##and operation
print(a)

a= arr1[(arr1!=5)|(arr1>5)]   #bitwise or operation
print(a)


a= arr1[(arr1!=4)|(arr1<4)]
print(a)



##EXAMPLE

arr=np.arange(1,26).reshape(5,5)
print(arr)

a = arr[2:5,1:5]
print(a)


a = arr[3,4]
print(a)


a = arr[0,1:3]
print(a)