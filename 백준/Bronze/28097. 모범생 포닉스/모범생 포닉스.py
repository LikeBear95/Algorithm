n = int(input())
l = list(map(int, input().split()))
s = sum(l)+8*(n-1)

print(s//24, s%24)