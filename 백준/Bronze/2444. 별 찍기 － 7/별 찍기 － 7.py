n = int(input())

# 위쪽 부분 출력
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# 아래쪽 부분 출력
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
