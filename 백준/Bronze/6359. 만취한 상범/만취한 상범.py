for _ in range(int(input())):
    n = int(input())
    l = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i,n+1,i):
            l[j] = 0 if l[j] else 1
    print(l.count(1))