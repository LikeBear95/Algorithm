lst = [0] * 26
for i in input():
    lst[ord(i)-97] += 1
print(*lst)