n = int(input())
s = input()
c = 0

for i in s:
    if i.isupper():
        c += 1
        break

for i in s:
    if i.islower():
        c += 1
        break

for i in s:
    if i in "!@#$%^&*()-+":
        c += 1
        break

for i in s:
    if i.isdecimal():
        c += 1
        break

print(max(6-len(s), 4-c))
