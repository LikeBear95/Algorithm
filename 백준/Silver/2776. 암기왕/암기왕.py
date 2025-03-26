for _ in range(int(input())):
    n = int(input())
    st = set(map(int, input().split()))
    m = int(input())
    lst = list(map(int, input().split()))
    for i in lst:
        print(1 if i in st else 0)