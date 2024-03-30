n = int(input())
lst = list(map(int, input().split()))
answer = 0
for i in range(n):
        tmp = []
        for j in range(1, lst[i]+1):
                if lst[i]% j == 0:
                        tmp.append(j)
        if len(tmp) == 2:
                answer += 1
print(answer)