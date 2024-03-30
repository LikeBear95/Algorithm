lst = []
for i in range(int(input()), int(input())+1):
        if i == 1:
                continue
        tmp = []
        for j in range(2, int(i**(1/2))+1):
                if i % j == 0:
                        tmp.append(j)
        if len(tmp) == 0:
                lst.append(i)

if lst:
        print(sum(lst))
        print(lst[0])
else:
        print(-1)