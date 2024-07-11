import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    tmp = input().rstrip()
    if tmp in dic:
        dic[tmp] += 1
    elif len(tmp) >= m:
        dic[tmp] = 1

for i, _ in sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(i)
