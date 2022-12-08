import numpy as np
from numpy import dtype

a = np.arange(10)
print(a)
b = np.arange(2,10)
print(b)
c=np.arange(2,20,4)
print(c)

d = np.zeros(5, dtype='int')
print(d)

e = np.zeros((2,3))
print(e)

f=np.ones(6)
print(f)

g=np.ones(6,dtype='int')
print(g)


h=np.ones((2,6))
print(h)

i=np.eye(3)
print(i)

j=np.identity(3)
print(j)

k = np.random.randint(1,20)  #randomly return one number within the given range
print(k)

l= np.random.randint(3) #random number from 0 to 2
print(l)

m = np.random.randn(3) # -1 to +1
print(m)

n = np.random.randn(5,5)  #  5*5 matrix
print(n)

arr_1 = np.arange(10)
print(arr_1)

o= arr_1.reshape(2,5) #x is rows --> y is column
print(o)

arr_2 = np.array([1,4,14,66,7,33,5])
print(arr_2)

#operation

p= arr_2.max()
print(p)
p= arr_2.min()
print(p)

p= arr_2.argmax() #max number space
print(p)
p= arr_2.argmin()
print(p)

#creating numpy using tuples

arr_3 = np.array((12,234,22,56))
print(arr_3)

print(arr_1)

q=arr_1*7
print(q)

q=arr_1 + arr_1
print(q)

q=arr_1 - arr_1
print(q)

q=np.array(arr_1 / 2, dtype='int') # type casting : converting into integer
print(q)
