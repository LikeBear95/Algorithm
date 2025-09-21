n = int(input())
l = list(map(int, input().split()))
x = 0

for i in range(n):
    if l[i] != i+1:
        x += 1

print(x)