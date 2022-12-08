import numpy as np

#list

my_list = [1,2,3,4,5]
print(type(my_list))

my_array = np.array(my_list)
print(type(my_array))

two_list = [[1,2],[3,4]]
two_list1 =\
    np.array(two_list)
print(type(two_list1))


ab = [1,2,3,4.0]
ab3 = np.array(ab)
print(type(ab3))

ab1 = [1,2,3,4,True]
ab2 = np.array(ab1)
print(type(ab2))