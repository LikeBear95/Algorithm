import sys
input = sys.stdin.readline

n, m = map(int, input().split())
six = 1000
one = 1000

for _ in range(m):
    a, b = map(int, input().split())
    if six > a: six = a
    if one > b: one = b

print(min(six, one * 6) * (n // 6) + min(six, one * (n % 6)))
