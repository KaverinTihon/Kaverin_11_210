from random import randint
countp=0
countn=0
stop=0
nums=[]
while stop==0:
    x=randint(0,9)
    nums.append(x)
    print('Try guess a number')
    y=int(input())
    if x==y:
        countp+=1
        print('Right!')
    else:
        countn+=1
        print('WRONG!')
    print('Try again?')
    no=str(input())
    if no=='no':
        print('% of right answers =',countp/(countn+countp)*100)
        for i in range(len(nums)):
                       print(nums[i])
        stop+=1
