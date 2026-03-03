n, k = map(int, input().split())
s = input()
m, c = 0, 0

for i in range(n):
    if s[i] == "0":
        c += 1
    else:
        c = 0
    m = max(c, m)

print(0 if m>=k else 1)