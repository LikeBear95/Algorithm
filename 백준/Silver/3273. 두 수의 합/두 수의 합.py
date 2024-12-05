n = int(input())
s = set(map(int, input().split()))
x = int(input())
a = 0
for i in s:
    if x-i in s:
        a += 1

print(a//2)