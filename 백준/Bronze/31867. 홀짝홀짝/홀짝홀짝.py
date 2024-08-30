n = int(input())
s = input()
odd = 0
even = 0
for i in range(n):
    if int(s[i]) % 2:
        odd += 1
    else:
        even += 1

if odd > even:
    print(1)
elif odd < even:
    print(0)
else:
    print(-1)