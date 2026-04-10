n = input()
c = 0

while len(n)!=1:
    n = str(sum([int(x) for x in n]))
    c += 1

print(c)
print("NO" if int(n)%3 else "YES")