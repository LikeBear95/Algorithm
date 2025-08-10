for _ in range(int(input())):
    n = int(input())
    t = n + int(str(n)[::-1])
    print("YES" if str(t) == str(t)[::-1] else "NO")