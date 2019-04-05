k = input("задайте числовые коэффиценты a,b,c через пробел: ")
k = k.split()
b = int(k[1])
a = int(k[0])
c = int(k[2])
D = b**2 - 4*a*c
if D < 0:
    print('корней нет')
if D == 0:
    print ((-b + D**(1/2))/(2*a))
if D> 0:
    print((-b + D**(1/2))/(2*a), (-b - D**(1/2))/(2*a))
     
    
