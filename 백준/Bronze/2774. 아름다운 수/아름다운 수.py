for _ in range(int(input())):
    n = int(input())
    s = set()
    for i in str(n):
        s.add(i)
    print(len(s))