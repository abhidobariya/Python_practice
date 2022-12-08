odd_count, even_count= 0,0
odd_total, even_total=0,0
no1 = int(input("enter start no:"))
no2 = int(input("enter last no:"))

for i in range(no1,no2+1):
    if (i%2)==0:
       even_count +=1
       print("even number count",even_count)
       even_total += i


    else:
       odd_count += 1
       print("odd number count",odd_count)
       odd_total += i



print("even number list:",even_total)
print("odd number list:",odd_total)

