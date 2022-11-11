num=(input("insert numbers separated by a space\n")).split(' ')
number=[int(x) for x in num]
ses= list(filter(lambda x: (x > 0), number))
n = 1
pr = lambda ses:ses[0] * pr(ses[1:]) if ses else 1
print(pr(ses))
