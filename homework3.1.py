def rectangle(x,z):
    for i in range(x+1):
        if i==0 or i==x:
            for j in range(z):
                print(sh,end='')
        else:
            print(sv,end='')
            for j in range(2,z):
                print(' ',end='')
            print(sv,end='')
        print()

x = int(input("Высота = "))
z = int(input("Ширина = "))
sh = input("Значок ширины:")
sv = input("Значок высоты:")

rectangle(x,z)
