l = [6]
n = int(input())
for i in range(11, n+1):
    l.append(l[-1]*i)
print(l[-1])