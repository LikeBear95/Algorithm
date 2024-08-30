for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    lst = []
    for i in tmp:
        if not i % 2:
            lst.append(i)
    print(sum(lst), min(lst))