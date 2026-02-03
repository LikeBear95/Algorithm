n, x = map(int, input().split())
s = sum(list(map(int, input().split())))
i = 0

while True:
    if (n+i)*x <= s+100*i:
        break
    i += 1

print(i)