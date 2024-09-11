lst = list(map(str, input().split()))
n = input()
answer = 0

for i in lst:
    if n == i[:len(n)] and len(n) != len(i):
        answer += 1

print(answer)