x=float(input())
y=float(input())
if abs(x)**2+abs(y)**2<=1:
    print('1')
elif abs(x)**2+abs(y)**2<=4:
    print('2')
elif abs(x)**2+abs(y)**2<=9:
    print('3')
elif abs(x)**2+abs(y)**2<=16:
    print('4')
elif abs(x)**2+abs(y)**2<=25:
    print('5')
elif abs(x)**2+abs(y)**2<=36:
    print('6')
elif abs(x)**2+abs(y)**2<=49:
    print('7')
elif abs(x)**2+abs(y)**2<=64:
    print('8')
elif abs(x)**2+abs(y)**2<=81:
    print('9')
elif abs(x)**2+abs(y)**2<=100:
    print('10')
else:
    print("Missed")
