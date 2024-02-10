import sys

# 테스트 케이스 개수 입력 받기
t = int(sys.stdin.readline())

# 각 테스트 케이스에 대해 반복
for _ in range(t):
    # 두 개의 수 입력 받기
    a, b = map(int, sys.stdin.readline().split())
    
    # 두 수의 합 출력
    print(a + b)
