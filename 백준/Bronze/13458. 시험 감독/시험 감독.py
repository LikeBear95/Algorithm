n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = n

for i in a:
    if i-b > 0:
        answer += (i-b)//c + (1 if (i-b)%c else 0)

print(answer)