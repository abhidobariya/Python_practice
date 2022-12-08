num = int(input("Enter the numbers:"))
i = 2
prime = True
if i in range(i,num):
    if(num%i==0):
        prime = False

if prime:
    print("This num is prime")
else:
    print("this num is not prime")