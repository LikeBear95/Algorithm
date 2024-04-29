lst = []
for _ in range(int(input())):
    tmp = input()
    lst.append(tmp)
lst = list(set(lst))
lst.sort(key=lambda x:(len(x), x))
for l in lst:
    print(l)