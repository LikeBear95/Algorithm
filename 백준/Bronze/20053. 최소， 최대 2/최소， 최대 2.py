for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    print(min(lst), max(lst))