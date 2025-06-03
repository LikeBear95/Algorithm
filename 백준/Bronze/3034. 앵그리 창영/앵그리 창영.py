n, w, h = map(int, input().split())

for _ in range(n):
    t = int(input())
    print("DA" if t**2 <= w**2 + h**2 else "NE")