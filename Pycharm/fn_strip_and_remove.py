def remove_and_split (string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    My name is abhi    "
print(this)
print(this.strip())
n = remove_and_split(this, "My")
print(n)

