lst = list(map(int, input().split()))
lst.sort()
for i in range(1, lst[2]+1):
    if i == lst[0] + lst[1]:
        print(lst[0]+lst[1]+i-1)
        break
else:
    print(sum(lst))