a = input("введите числа через пробел:")
a = a.split()
for i in range(0, len(a)):
    if (i<len(a) and a[i]>a[i-1]):
        print(a[i])
    i+=1

