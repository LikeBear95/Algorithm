import sys
input = sys.stdin.readline

t = 0
for i in range(int(input())):
    t += sum(list(map(int, input().split())))

print(t)