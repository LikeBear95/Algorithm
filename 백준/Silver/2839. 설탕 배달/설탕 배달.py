n = int(input())
answer = 0

for i in range(n//5 + 1):
    if not (n - 5 * (n//5 - i)) % 3:
        answer = n//5 - i + (n - 5 * (n//5 - i)) // 3
        break

if answer:
    print(answer)
else:
    print(-1)