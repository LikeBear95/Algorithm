t, x = map(int, input().split())
n = int(input())
for _ in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    if not x in a:
        print("NO")
        break
else:
    print("YES")