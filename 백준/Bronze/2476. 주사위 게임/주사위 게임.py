import sys
input = sys.stdin.readline

answer = 0

for i in range(int(input())):
    lst = list(map(int, input().split()))
    if len(set(lst)) == 1:
        prize = 10000 + 1000 * max(lst)
    elif len(set(lst)) == 3:
        prize = 100 * max(lst)
    else:
        for i in lst:
            if lst.count(i) == 2:
                prize = 1000 + i * 100
                break
    if answer < prize:
        answer = prize

print(answer)