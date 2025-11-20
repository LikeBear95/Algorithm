a = input()
b = list(map(str, input().split()))

for i in b:
    a = a.replace(i, i.lower())

print(a)