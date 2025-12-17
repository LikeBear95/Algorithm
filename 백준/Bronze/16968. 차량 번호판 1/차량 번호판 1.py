s = input()
n = 1

for i in range(len(s)):
    if s[i] == 'c':
        if i > 0 and s[i-1] == 'c':
            n *= 25
        else:
            n *= 26
    else:
        if i > 0 and s[i-1] == 'd':
            n *= 9
        else:
            n *= 10

print(n)
