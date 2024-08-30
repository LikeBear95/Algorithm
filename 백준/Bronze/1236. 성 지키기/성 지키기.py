import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = [x for x in range(n)]
M = [x for x in range(m)]

MAP = [input().rstrip() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if MAP[i][j] == "X":
            if i in N:
                N.remove(i)
            if j in M:
                M.remove(j)

print(max(len(N), len(M)))
