myDict = {
        "Pankha":"Fan",
        "Vastu":"Item",
        "Dabba":"Box",
        "Ghada":"Pot"
        }
print("Options are :",myDict.keys())
a = input("Enter your chose option:\n")
print("The meaning of your word is:", myDict.get(a))



#unique numbers (set)

num1 =int(input("Enter number:"))
num2 =int(input("Enter number:"))
num3 =int(input("Enter number:"))
num4 =int(input("Enter number:"))
num6 =int(input("Enter number:"))
num7 =int(input("Enter number:"))
num5 =int(input("Enter number:"))
num8 =int(input("Enter number:"))

s = {num1,num2,num3,num4,num5,num6,num7,num8}
print(s)



#
s= {18 ,"18"}
print(s)


#
s ={20 , 20.0 , "20"}
print (s)
print(len(s))


#
favLang={}

a= input("Enter your Favourit language Abhi\n")
b= input("Enter your Favourit language Karan\n")
c= input("Enter your Favourit language Mayank\n")
d= input("Enter your Favourit language Rakesh\n")

favLang['abhi']=a
favLang['karan']=b
favLang['mayank']=c
favLang['rakesh']=d

print(favLang)








