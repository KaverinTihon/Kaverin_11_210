x=input()+'.'
s=[]
z=x[0]
c=1
for i in x[1:]:
    if i!=z:
        s.append(z)
        if c>1:
            s.append(c)
        z=i
        c=1
    else:
        c+=1
print(*s)
