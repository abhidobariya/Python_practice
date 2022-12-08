def CheckLeap(year):
    if((year%400==0)or(year%100!=0)and(year%4==0)):
        print("this year is leap year")
    else:
        print("this year is not leap year")

year = int(input("Enter the number"))
CheckLeap(year)