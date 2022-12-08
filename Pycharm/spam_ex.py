text = input("Enter the text\n")

if("make a loat of money\n" in text):
    spam = True
elif("buy now\n"in text):
    spam = True
elif("Click this\n"in text):
    spam = True
elif("Subscribe this \n" in text ):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
