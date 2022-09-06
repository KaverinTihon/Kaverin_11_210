f='2312312321213231232132454452413437658798098464'
c=0
a=str(input())
while a in f:
    f=f.replace(a,'',1)
    c+=1
print(c)      
