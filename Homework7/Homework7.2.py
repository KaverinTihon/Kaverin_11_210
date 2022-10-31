import re
names=input('С большой буквы и черз пробел\n').split(', ')
fcounter=0
mcounter=0
def female(lastNames):
    endfe=["ова", "ева", "ина", "ына", "ская", "цкая"]
    count=0
    for i in endfe:
        if re.search(fr'\B{i}$',lastNames) != None:
            count+=1
    return(count)
def male(lastNames):
    endma = ["ов", "ев", "ин", "ын", "ский", "цкий"]
    count = 0
    for i in endma:
        if re.search(fr'\B{i}$',lastNames) != None:
            count+=1
    return(count)
for j in names:
    fcounter+=female(j)
    mcounter+=male(j)
print(fcounter)
print(mcounter)
