def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high)//2
        if data[middle] == elem:
            print(middle)
            return 0
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    print('Not found')
    return 0
mass=[00,11,22,33,44,55,66,77,88,99]
x=int(input())
binary_search(mass,x)
