import sys

def dfs(lst):
    if len(lst) == m:
        print(*lst)
    else:
        for i in num:
            lst.append(i)
            dfs(lst)
            lst.pop()


n, m = map(int, input().split())
num = [x for x in range(1, n+1)]
dfs([])
