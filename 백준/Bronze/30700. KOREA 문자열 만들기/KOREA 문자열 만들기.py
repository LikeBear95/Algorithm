s = "KOREA"
n = 0

for i in input():
    if i == s[n%5]:
        n += 1

print(n)