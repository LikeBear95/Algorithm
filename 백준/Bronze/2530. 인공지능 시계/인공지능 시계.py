a, b, c = map(int, input().split())
d = int(input())
s = 3600 * a + 60 * b + c + d
print(s // 3600 % 24, s // 60 % 60, s % 60)