myDict = {
        "Abhi":"student",
        "Marks":[70,80,90]
        }

#Dictionary Method

print(myDict.keys())
print(myDict.values())
print(myDict.items())

updateDict = {
        "rohan":"frd",
        "vivek":"frd",
        "yash":"frd"
        }
myDict.update(updateDict)
print(myDict)

print(myDict.get("Abhi"))
print(myDict.get("Abhi2"))

