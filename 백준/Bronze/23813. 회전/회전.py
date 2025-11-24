n = int(input())
s = str(n)*2
l = len(s)//2
m = 0

for i in range(l):
    m += int(s[i:i+l])

print(m)