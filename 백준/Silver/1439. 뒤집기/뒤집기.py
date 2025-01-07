s = input()
n = s[0]
cnt = 1

for i in s[1:]:
    if n != i:
        n = i
        cnt += 1

print(cnt//2)