def percent (marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [90,70,68,88]
percentage1 = percent(marks1)

marks2 = [70,79,58,88]
percentage2 = percent(marks2)

print(percentage1,percentage2)