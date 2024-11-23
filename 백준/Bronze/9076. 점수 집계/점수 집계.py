for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    print("KIN" if lst[3]-lst[1] >= 4 else sum(lst[1:4]))