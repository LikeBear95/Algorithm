s = input()
n = 1
t = 1

for i in range(1, len(s)):
    if s[i] > s[i-1]:
        t += 1
    else:
        t = 1
    n += t

print(n)