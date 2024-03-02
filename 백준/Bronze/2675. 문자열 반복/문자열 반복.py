for _ in range(int(input())):
    r, s = map(str, input().split())
    r = int(r)
    tmp = ''
    for i in s:
        tmp += i * r
    print(tmp)