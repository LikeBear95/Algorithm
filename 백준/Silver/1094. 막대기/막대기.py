import sys
input = sys.stdin.readline

n = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
answer = 0

for i in stick:
    if n >= i:
        n -= i
        answer += 1

print(answer)
