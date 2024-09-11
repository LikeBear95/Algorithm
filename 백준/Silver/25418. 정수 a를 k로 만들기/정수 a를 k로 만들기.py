a, b = map(int, input().split())
answer = 0
while a != b:
    if b % 2:
        b -= 1
    elif b // 2 >= a:
        b //= 2
    else:
        b -= 1
    answer += 1

print(answer)