n = int(input())
lst = list(map(int, input().split()))
tmp = 0
answer = 0
for i in lst:
    if i == 1:
        tmp += 1
        answer += tmp
    else:
        tmp = 0
        
print(answer)