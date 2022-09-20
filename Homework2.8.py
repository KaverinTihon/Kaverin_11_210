x=int(input())
s=0
i=0
while x:
    s+=(x%10)*2**i
    i+=1
    x//=10
print(s)
