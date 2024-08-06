lst = [x**2 for x in range(1, 101)]
m = int(input())
n = int(input())
answer = []
for i in lst:
    if i >= m and i <= n:
        answer.append(i)
    elif i > n:
        break

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)