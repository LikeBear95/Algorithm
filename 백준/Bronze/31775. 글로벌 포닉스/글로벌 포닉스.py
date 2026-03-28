import sys
input = sys.stdin.readline

a = {'l','k','p'}
b = set()

for _ in range(3):
    t = input().rstrip()
    b.add(t[0])

print("GLOBAL" if a == b else "PONIX")