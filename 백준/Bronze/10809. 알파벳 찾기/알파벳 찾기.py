lst = [0] * 26
S = input()
for i in range(26):
    if chr(97+i) in S:
        lst[i] = S.index(chr(97+i))
    else:
        lst[i] = -1
print(*lst)