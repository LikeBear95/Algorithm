n = int(input())
if n == 0:
    print("divide by zero")
else:
    l = list(map(int, input().split()))
    s = set(l)
    print(f'{(sum(l)/len(l))/sum([x*(l.count(x)/len(l)) for x in s]):.2f}')