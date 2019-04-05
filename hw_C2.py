a = str(int(input("введите число:   ")))
sum_of_digits = sum(int(digit) for digit in a)
print(f' число : {a}, сумма цифр числа: {sum_of_digits}')
total = 1
for i in range(0, len(a)):
    total *= int(a[i])
print(f' умножение цифр числа: {a} равно {total}')

    
        
          
                        





        
