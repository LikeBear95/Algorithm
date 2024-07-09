import sys
input = sys.stdin.readline

hi = set()
answer = 0

for _ in range(int(input())):
    tmp = input().rstrip()
    if tmp == "ENTER":
        answer += len(hi)
        hi = set()
    else:
        hi.add(tmp)

print(answer + len(hi))
