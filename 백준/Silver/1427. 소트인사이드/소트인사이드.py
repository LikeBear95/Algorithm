n = input()
lst = []
for i in n:
    lst.append(i)
print(''.join(sorted(lst)[::-1]))