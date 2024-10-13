import sys
input = sys.stdin.readline

for _ in range(int(input())):
    lst = list(map(str, input().split()))
    new_lst = [x[::-1] for x in lst]
    print(' '.join(new_lst))