def Sum_iterative(n):
   sum = 0
   for i in range( 1 , n+1):
      sum = sum + i
   return sum

def Sum_recursive(n):
   sum = Sum_iterative(n-1) + n
   return sum

n = int(input("Enter Number\n"))
print(Sum_recursive(n))