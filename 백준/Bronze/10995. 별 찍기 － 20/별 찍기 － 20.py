n = int(input())
s = " *"*n

for i in range(n):
    print(s if i%2 else s[1:])