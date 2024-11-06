import sys
input = sys.stdin.readline

lst = []
for i in range(9):
    lst.append(int(input()))

n = sum(lst)
for i in range(8):
    for j in range(i+1, 9):
        if n - lst[i] - lst[j] == 100:
            for k in lst:
                if k not in [lst[i],lst[j]]:
                    print(k)
            break