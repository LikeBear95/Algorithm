X = int(input())
total = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    total += a * b

if X == total:
    print("Yes")
else:
    print("No")