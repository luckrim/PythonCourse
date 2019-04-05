# Определить длину самого короткого слова в строке, заданной пользователем
a = str(input("введите строку:"))
a = a.split()
for i in range(1, len(a)):
    if (i<len(a) and len(a[i])<len(a[i-1])):
        print(len(a[i]))
    i+=1
