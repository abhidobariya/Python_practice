x= "nice"
def myfunc():

  x = "good"
  print("this is "+x)
myfunc()
print("this is "+x)

x=5
y=10
print(x+y)

x=b"hello"
print(type(x))

x= {"abc", "pqr"}
print(type(x))

x=("abc","abc")
print(type(x))

x=['abc','abc']
print(type(x))

x=frozenset({"abc","abc"})
print(type(x))

x="hyiii"
print(type(x))

x=1
y=2.1
z=3j
print(type(x))
print(type(y))
print(type(z))

#type conversion

x=4
y=3.4
z=5j

a=float(x)
b=int(y)
c=complex(x)


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


x= "hello world!"
print(x[4])



#loop
for x in "apple":
  print(x)


txt= "hello i am abhi"
print("wood" in txt)



txt="i am using laptop"
if "good" in txt:
  print("yse 'am' is present")
  

#check if not

txt="hello goodmorning guys"
print("hello" not in txt)



