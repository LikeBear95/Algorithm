import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = input().strip()
    print("Yes" if t.lower() == t[::-1].lower() else "No")
