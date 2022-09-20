#x=int(input())
#i=0
#c=1
#t=x
#while t:
#   t//=10
#   c*=10
#while x:
#    c//=10
#    i+=x%10*c
#    x//=10
#print(i)
x=int(input())
c=10
print("=")
while x:
    print(x%c)
    i=x%c
    print("+")
    c*=10
    x-=i
