n = int(input())
l = [1, 5, 12, 22]

for i in range(4, n+1):
    l.append((l[-1]+3*i+1)%45678)

print(l[n])