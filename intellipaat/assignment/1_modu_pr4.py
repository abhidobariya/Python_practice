# arr1 = [1,2,3,4,5,6,7]
# arr2 = [5,4,3,7,8,9,1]
# for i in arr1:
# if i in arr2:
#     print(i)

# def abc(a,b):
#     for a in range(1,5):
#         for b in range(1,5):
#             for i in a :
#                 for j in b:
#                     if i == j:
#                         print(i)

lst1 = [1,2,3,4,8,7]
lst2 = [1,6,7,8,9]
lst3=[]
def abc (lst1,lst2):
    for i in range(len(lst1)):
        for j in range (0,len(lst2)):
            if lst1[i] == lst2[j]:
                lst3.append(lst2[j])
    print (lst3)
abc(lst1,lst2)

