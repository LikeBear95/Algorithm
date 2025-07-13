for _ in range(int(input())):
    n = int(input())
    print("YES" if str(n)==str(n**2)[-len(str(n)):] else "NO")