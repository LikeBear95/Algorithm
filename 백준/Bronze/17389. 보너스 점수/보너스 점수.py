n = int(input())
p = input()
s, b = 0, 0

for i in range(n):
    if p[i] == "O":
        s += i+1+b
        b += 1
    else:
        b = 0

print(s)