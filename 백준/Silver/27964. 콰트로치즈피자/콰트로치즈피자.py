import sys
input = sys.stdin.readline

n = int(input())
s = set(map(str, input().rstrip().split()))
answer = 0

for i in s:
    if i[-6:] == "Cheese":
        answer += 1

print("yummy" if answer >= 4 else "sad")
