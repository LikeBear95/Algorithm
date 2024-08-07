import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    tmp = list(map(str, input().rstrip().split()))
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    tmp[3] = int(tmp[3])
    lst.append(tmp)

new_lst = sorted(lst, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in new_lst:
    print(i[0])