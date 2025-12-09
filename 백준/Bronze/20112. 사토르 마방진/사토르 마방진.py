import sys
input = sys.stdin.readline

n = int(input())
l = list(input().rstrip() for _ in range(n))

for i in range(n):
    for j in range(i):
        if l[i][j] != l[j][i]:
            print("NO")
            exit(0)

print("YES")