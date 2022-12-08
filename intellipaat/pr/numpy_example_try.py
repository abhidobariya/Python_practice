#1
import numpy as np

#2
a=np.zeros(10)
print(a)

#3
b=np.ones(10)
print(b)

#4
c=np.ones(10)*5
print(c)

#4 (2nd method)
c=np.full(10,5, dtype=float)
print(c)

    #4.1
c=np.full((2,3),'ABHI')
print(c)

#5
d= np.arange(10,50)
print(d)
print(type(d))

#6 (even numbers)
e = np.arange(10,50)
print(e[e %2 == 0])

    #6
e = np.arange(10,50)%2 == 0
print(e[e])

    #6

e = np.arange(10,50, 2)
print(e)

#7  (Create a 3*3 identity matrix)

f = np.eye(3)
print(f)

    #7

f = np.identity(3)
print(f)

#8 (random number between 0 to 1) --> not noraml distribution

g= np.random.randn(1)
print(g)

#9 (use numpy to generat an array of 25 random numbers sampled from a standard normal distribution)

h = np.random.randn(25)
print(h)


#10  (5*5 matrix)

i= np.arange(1,26).reshape(5,5)
print(i)