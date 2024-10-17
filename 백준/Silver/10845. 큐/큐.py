import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    tmp = input().rstrip()
    if tmp == "back":
        print(lst[-1] if lst else -1)
    elif tmp == "front":
        print(lst[0] if lst else -1)
    elif tmp == "empty":
        print(0 if lst else 1)
    elif tmp == "size":
        print(len(lst))
    elif tmp == "pop":
        print(lst.pop(0) if lst else -1)
    else:
        lst.append(int(tmp[5:]))