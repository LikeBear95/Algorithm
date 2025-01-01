for _ in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0]
    cnt = len([x for x in lst[1:] if x > avg])
    answer = cnt / lst[0] * 100
    print(f"{answer:.3f}%")
