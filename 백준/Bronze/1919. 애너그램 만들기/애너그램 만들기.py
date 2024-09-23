import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

dic_a = {}
dic_b = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
answer = 0

for i in a:
    if i in dic_a:
        dic_a[i] += 1
    else:
        dic_a[i] = 1

for i in b:
    if i in dic_b:
        dic_b[i] += 1
    else:
        dic_b[i] = 1

for i in alpha:
    if dic_a.get(i, 0) != dic_b.get(i, 0):
        answer += abs(dic_a.get(i, 0) - dic_b.get(i, 0))

print(answer)