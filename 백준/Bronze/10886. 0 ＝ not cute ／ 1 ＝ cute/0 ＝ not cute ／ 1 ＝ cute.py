import sys
input = sys.stdin.readline

n = int(input())
a = 0
for _ in range(n):
    a += int(input())

print("Junhee is cute!" if a > n//2 else "Junhee is not cute!")