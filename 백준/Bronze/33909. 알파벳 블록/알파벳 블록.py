s, c, o, n = map(int, input().split())
s = s+n
c = c + 2 * o
print(min(s//3, c//6))