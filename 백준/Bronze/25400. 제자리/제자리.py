n = int(input())
A = list(map(int, input().split()))

target = 1
for num in A:
    if num == target:
        target += 1

print(n - (target - 1))
