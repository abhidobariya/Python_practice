letter = '''Dear <|NAME|>,
You are selected!
Greeting from abc codinf house.
Have a great day ahead!

Date: <|DATE|>
'''

name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
