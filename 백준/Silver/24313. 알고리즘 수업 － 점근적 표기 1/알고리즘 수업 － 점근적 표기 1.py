A, a = map(int, input().split())
c = int(input())
n = int(input())

for i in range(n, 101):
    if a + A*i > c * i:
        print(0)
        break
else:
    print(1)