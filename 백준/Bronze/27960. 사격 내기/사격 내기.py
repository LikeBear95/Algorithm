a, b = map(int, input().split())
a, b = bin(a)[2:], bin(b)[2:]
a, b = '0'*(10-len(a))+a, '0'*(10-len(b))+b
c = 0

for i in range(10):
    if a[i] != b[i]:
        c += 2**(9-i)
print(c)