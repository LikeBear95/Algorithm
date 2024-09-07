n, m = map(int, input().split())
answer = 0
for i in range(n):
    s = input()
    if s.count("O") > m//2:
        answer += 1
print(answer)