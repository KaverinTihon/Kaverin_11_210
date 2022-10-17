k=int(input())
s=0
while k:
    s+=k%10
    k//=10
print(s)
