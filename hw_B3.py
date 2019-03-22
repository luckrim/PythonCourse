with open('rosalind_hamm.txt', 'r') as file:
    a = file.read()
b = a.split('\n')
k = str(b[0])
l = str(b[1])
count = 0
for c1, c2 in zip(k, l):
    if c1!=c2:
        count+=1
print(count)

