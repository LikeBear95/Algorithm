n = int(input())
s = input()
x = 0

for i in s:
    x += ord(i)-64

print(x)