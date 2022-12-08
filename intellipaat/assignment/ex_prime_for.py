# n=(int(input("enter no.")))
# flag=0
# n = []
#
# for i in range(0,5):
#        n.append(int(input("enter number .")))
#        flag =1
#
#        for j in range(2,i):
#               if (i%j)==0:
#                      flag=1
#        if(flag==0):
#               print(i,"is prime no")
#
a= []
b= []
a= int(input("Please, Enter the Lowest Range Value: "))
b = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
for number in range(a, b + 1):

       if number > 1:
              for i in range(2, number):
                     if (number % i) == 0:
                       break
              else:
                     print([number])