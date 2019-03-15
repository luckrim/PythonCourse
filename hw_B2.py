with open('man.txt', 'r') as file:
    a = file.read()
a=a[::-1]
for char in a:
    if char == 'T':
        a =(a.replace('T','t'))
for char in a:
    if char == 'A':
        a = a.replace('A', 'T')
for char in a:
    if char == 't':
        a = a.replace('t', 'A')
for char in a:
    if char == 'G':
        a = a.replace('G', 'g')
for char in a:
    if char == 'C':
        a = a.replace('C', 'G')
for char in a:
    if char =='g':
        a = a.replace('g','C')
print(a)
        






