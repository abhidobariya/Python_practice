#multiple name replace

with open(f"name_replace_r_w_fn.txt")as f:
    content = f.read()

content= content.replace("donkey","@#$%&¨^")

with open("name_replace_r_w_fn.txt","w")as f:
    content = f.write(content)

#list replace

words = ["donkey", "motu","patalu"]
with open(f"name_replace_r_w_fn.txt")as f:
    content = f.read()
for word in words:
    content= content.replace(word,"@#$%&¨^")
    with open("name_replace_r_w_fn.txt","w")as f:
        f.write(content)