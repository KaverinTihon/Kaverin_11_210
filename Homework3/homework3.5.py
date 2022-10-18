n=int(input())
s=0
for i in range(n):
    x=1
    for y in range(i+1):
        x*=y+1
    s+=x
print(s)
