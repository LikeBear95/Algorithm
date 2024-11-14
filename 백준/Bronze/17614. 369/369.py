a = 0
for i in range(1, int(input())+1):
    s = str(i)
    a += s.count('3')
    a += s.count('6')
    a += s.count('9')

print(a)