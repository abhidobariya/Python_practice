a = [1,2,3,4,5,6,7]
def even(a):
    new_a = []
    for i in a:
        if i%2==0:
            new_a.append(i)
    return new_a
print(even(a))
