import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in str(n):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic['6'] = dic.pop('6', 0) + dic.pop('9', 0)
dic['6'] = dic.get('6') // 2 + 1 if dic.get('6') % 2 else dic.get('6') // 2

print(max(dic.values()))
