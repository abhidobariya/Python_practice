sub1 = int(input("Enter first subject marks:\n"))
sub2 = int(input("Enter second subject marks:\n"))
sub3 = int(input("Enter third subject marks:\n"))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("Sorry!.. you are FAIL")
elif (sub1 + sub2 + sub3) / 3 < 40:
    print("you are fail bcz your pr less-then 40")
else:
    print("cong... you are pass")
