import random
names=['Aline','Bratt','Conor','Draven','Ena',
       'Fred','Gloria','Honey','Isaac','Jojo',
       'Klare','Lorens','Mundo','Nines','Oriana',
       'Aline','Bratt','Conor','Draven','Ena']
sam=random.choices(names,k=20)
div2=random.choices(names,k=20)
div3=random.choices(names,k=20)
a=set(div3)
b=set(div2)
c=set(sam)
i=a&b&c
print(sam)
print(div2)
print(div3)
if i==set():
    print('0 found')
else:
    print(i)
if ((a^b^c)-i)==set():
    print('0 found')
else:
    print((a^b^c)-i)
