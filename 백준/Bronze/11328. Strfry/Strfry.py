import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(str, input().rstrip().split())
    print("Possible" if sorted(a) == sorted(b) else "Impossible")