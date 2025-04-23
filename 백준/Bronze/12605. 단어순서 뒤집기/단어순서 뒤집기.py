import sys
input = sys.stdin.readline

for i in range(int(input())):
    lst = list(map(str, input().rstrip().split()))
    print(f'Case #{i+1}:', *lst[::-1])