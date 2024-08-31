lst = [0]
used = set(lst)

for i in range(1, int(input())+1):
    num = lst[i-1] - i
    if num < 0 or num in used:
        num = lst[i-1] + i
    lst.append(num)
    used.add(num)

print(lst[-1])