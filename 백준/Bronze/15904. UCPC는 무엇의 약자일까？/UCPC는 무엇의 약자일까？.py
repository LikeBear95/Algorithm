s = input()
t = "UCPC"
n = 0

for i in s:
    if t[n] == i:
        n += 1
    if n == 4:
        break

print("I love UCPC" if n == 4 else "I hate UCPC")