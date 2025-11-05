for i in range(int(input())):
    t = input()
    n = int(input())
    m = 0
    for j in range(n):
        m += int(input())
    print("NO" if m%n else "YES")