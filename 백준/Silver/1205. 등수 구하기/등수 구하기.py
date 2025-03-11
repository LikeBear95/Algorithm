n, s, p = map(int, input().split())
lst = list(map(int, input().split())) if n else []

if n == p and s <= min(lst):
    print(-1)
else:
    lst.append(s)
    lst.sort(reverse=True)
    print(lst.index(s)+1)
