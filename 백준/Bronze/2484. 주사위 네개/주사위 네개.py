import sys
input = sys.stdin.readline

m = 0
for _ in range(int(input())):
    l = list(map(int, input().split()))
    s = set(l)
    if len(s) == 4:
        m = max(m, max(l)*100)
    elif len(s) == 1:
        m = max(m, 50000 + l[0]*5000)
    elif len(s) == 3:
        for i in s:
            if l.count(i) == 2:
                m = max(m, 1000 + i*100)
                break
    else:
        a, b = map(int, s)
        if l.count(a) == 2:
            m = max(m, 2000 + (a+b)*500)
        else:
            m = max(m, 10000 + (a if l.count(a)==3 else b)*1000)

print(m)